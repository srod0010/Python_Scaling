Introduction to Group Membership
Understand core principles of group membership in distributed Python applications. Learn how to track cluster liveliness, balance workloads, and ensure high availability using the Tooz library's abstractions and algorithms. This lesson equips you with the knowledge to implement effective cluster coordination in scalable systems.

Distributed applications all show the same set of well-known problems that they need to solve. One of them is distributed locking of resources so that no resource inadvertently gets shared access, as discussed in the previous chapter (Lock Management). The second one involves cluster membership awareness and liveliness.

A typical use case for distributed workers is the need to know how many workers are alive in the cluster. This data allows for implementing different scenarios, such as high availability (one node doing the work and the other one standing-by) and load balancing (several nodes spreading some work across each other).

In all cases, an external service is needed to achieve this functionality. Rather than picking one and implementing all those low-level features in your application, this chapter demonstrates how to use the abstraction layer and algorithms that the Tooz library provides to solve that efficiently.
