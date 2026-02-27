# Creating, Joining, and Leaving Groups (Tooz)

Lesson focus:
- A group is a set of zero or more members.
- Nodes can create a group, join it, and leave it.
- Membership liveness is maintained by Tooz heartbeat + backend state.
- Backends matter: stronger coordination backends generally provide stronger robustness.

Reference lesson:
https://www.educative.io/courses/hackers-guide-scaling-python/introduction-to-functional-programming

Project runbook (setup/install/service management):
`/Users/saviorodrigues/Documents/Python_Scaling/README.md`

## Files in this folder

- `tooz_join_group.py`: annotated runnable example based on the lesson workflow.

## Setup

From repo root (`/Users/saviorodrigues/Documents/Python_Scaling`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run with etcd

1. Start etcd in terminal A:

```bash
etcd --data-dir /tmp/etcd-data
```

2. In terminal B, run client A:

```bash
cd /Users/saviorodrigues/Documents/Python_Scaling/python_scaling/group_membership
python tooz_join_group.py clientA group1
```

3. In terminal C, run client B (same group):

```bash
cd /Users/saviorodrigues/Documents/Python_Scaling/python_scaling/group_membership
python tooz_join_group.py clientB group1
```

Both clients should print membership lists that include both members while both are active.

If you pass backend URL explicitly, use:

```bash
python tooz_join_group.py clientA group1 etcd3+http://localhost
```

## Run with memcached

1. Start memcached in terminal A:

```bash
memcached -u memcache
```

If that user does not exist on your machine, run:

```bash
memcached
```

2. In terminal B, run client A with memcached backend URL:

```bash
cd /Users/saviorodrigues/Documents/Python_Scaling/python_scaling/group_membership
python tooz_join_group.py clientA group1 memcached://localhost:11211
```

3. In terminal C, run client B:

```bash
cd /Users/saviorodrigues/Documents/Python_Scaling/python_scaling/group_membership
python tooz_join_group.py clientB group1 memcached://localhost:11211
```

## What the script demonstrates

1. Creates a coordinator and starts heartbeat (`start_heart=True`).
2. Creates the group (`create_group`), ignoring "already exists".
3. Joins the group (`join_group`).
4. Reads active members (`get_members`).
5. Waits 60 seconds to keep membership visible.
6. Leaves the group (`leave_group`) and stops coordinator.

## Notes on async API

Tooz operations are asynchronous. Methods like `create_group`, `join_group`, and `leave_group` return futures.  
Calling `.get()` waits for completion, which is required before assuming operation success.
