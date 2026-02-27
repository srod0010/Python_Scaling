#!/usr/bin/env python3
"""
Creating, joining, listing, and leaving a Tooz group.

Default backend URL is etcd3+http://localhost.
You can override with:
  1) third CLI argument, or
  2) TOOZ_BACKEND_URL environment variable.
"""

import os
import sys
import time

from tooz import coordination


def main() -> int:
    # Keep the original lesson behavior: require client_id and group_id.
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(
            "Usage: %s <client id> <group id> [backend url]"
            % sys.argv[0]
        )
        print("Example etcd:      python tooz_join_group.py clientA group1")
        print(
            "Example memcached: python tooz_join_group.py "
            "clientA group1 memcached://localhost:11211"
        )
        return 1

    client_id = sys.argv[1].encode()
    group = sys.argv[2].encode()

    # Priority: CLI backend URL > env var > lesson default.
    backend_url = (
        sys.argv[3]
        if len(sys.argv) == 4
        else os.getenv("TOOZ_BACKEND_URL", "etcd3+http://localhost")
    )

    # Compatibility shim: older examples often use etcd3://localhost.
    # Current Tooz registers etcd3+http and etcd3+https drivers.
    if backend_url.startswith("etcd3://"):
        backend_url = backend_url.replace("etcd3://", "etcd3+http://", 1)

    print(f"[info] backend={backend_url}, client={sys.argv[1]}, group={sys.argv[2]}")

    # Create coordinator client and start heartbeat so membership stays alive.
    coordinator = coordination.get_coordinator(backend_url, client_id)
    coordinator.start(start_heart=True)

    try:
        # Create the group once. Ignore "already exists" if another node created it.
        try:
            coordinator.create_group(group).get()
            print("[info] group created")
        except coordination.GroupAlreadyExist:
            print("[info] group already exists")

        # Tooz APIs are async; .get() waits for completion.
        coordinator.join_group(group).get()
        print("[info] joined group")

        members = coordinator.get_members(group).get()
        decoded_members = sorted(m.decode() for m in members)
        print(f"[info] members now: {decoded_members}")

        # Keep this member alive in the group for observation.
        print("[info] sleeping for 60 seconds before leaving...")
        time.sleep(60)

        coordinator.leave_group(group).get()
        print("[info] left group")
        return 0
    finally:
        coordinator.stop()
        print("[info] coordinator stopped")


if __name__ == "__main__":
    raise SystemExit(main())
