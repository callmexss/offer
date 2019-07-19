## Test Case

### Functional Test：

```text
1->1->2, 2  # duplicated at begining
1->2->2, 1  # duplicated at ending
1->2->2->2->3, 1->3  # duplicated in the middle
1->2->2->3->3->4, 1->4  # continous duplicated elements in the middle
1->2->3, 1->2->3  # with out duplicated elements
```

### Special Cases：

```text
None, None  # empty input
1->1->1, None # all the elements are duplicated
```

## Thinking

### Step 1

First considerate the simplist situation,

```python
1->2->3

# add a head node will make things easier,
# so suppose we have a new head with value 0.

0->1->2->3

head->1
new_head->0

pre->0 
cur->1

# because none of them are duplicated,
# so we just traverse the linked list.

while cur:
    pre = cur
    cur = cur.next
```

### Step 2

So what's happen when there are duplicated elements?
Short to say, we just need to find a suitable location for cur to points to.

```
# 0 is an extra added node 
0->1->1->2

head->1
new_haed->0

pre->0
cur->1

while cur:

    # if we can make cur points to 2
    # then just let pre.next points cur
    # which means there are no duplicated numbers
    # between pre and cur 
    # now we can forward to next loop

    inner_cur = cur
    duplicated = 0  # record duplicated

    # find a suitable location for cur in an inner loop
    while inner_cur:
        if inner_cur.val == inner_cur.next.val:
            # duplicated
            inner_cur = inner_cur.next
            duplicated += 1
        else:  # current val is not equal to next val
            if duplicated:  # make current point to next un-duplicated val
                inner_cur = inner_cur.next
                break
            else:  # do nothing, leave things to outer loop (Step 1)
                break

    cur = inner_cur  # cur will change if there are duplicated numbers else won't.

    # so
    if duplicated:
        # cur has points to 2 and we know there are duplicated numbers
        # since we have make cur and pre change to their right location
        # just continue the loop
        pre.next->cur
        continue
    else:  # do things in the step 1
        pre = cur
        cur = cur.next
```

### Step 3

Take special things in to consideration.

```python
0->1->2->2

inner_cur = cur
duplicated = 0  # record duplicated
while inner_cur:
    # if cur do not have a next node
    # this operation will cause an Exception
    # so check if cur has next node first
    if inner_cur.val == inner_cur.next.val:
        ...

# modification inner loop

inner_cur = cur
duplicated = 0  # record duplicated
while inner_cur:
    if inner_cur.next:
        if inner_cur.val == inner_cur.next.val:
            # points to next node
            inner_cur = inner_cur.next
            # records duplicated
            duplicated +=1
        else:  # current val is not equal to the next val
            if duplicated:
                # let inner_cur move forward 
                # so it traverses all the duplicated numbers
                inner_cur = inner_cur.next
            else:  # THERE ARE NO DUPLICATED NUMBERS SO DO NOTHING
                # do not modify cur's location
                break
    else:  # the next node is None
        if duplicated:
            # move forward inner_cur
            inner_cur = inner_cur.next
        else:  # THERE ARE NO DUPLICATED NUMBERS SO DO NOTHING
            break
```

### Step 4

Make all the things together.

```python
def deleteDuplication(self, pHead):
    mHead = ListNode(0)
    mHead.next = pHead
    pre = mHead
    cur = pHead
    while cur:
        inner_cur = cur
        duplicated = 0
        # use inner_cur find a suitable location
        # if no duplicated, do not change original cur
        # else find the next un-duplicated node
        # than make cur points to inner_cur
        # for example,
        # 1->2, do nothing
        # pre = cur
        # cur = cur.next
        # 1->1->2, let inner_cur point to 2
        # cur = inner_cur
        # pre.next = cur
        # noted that cur's location has been changed
        # so do not change it again
        while inner_cur:
            if inner_cur.next:  # not the last one
                if inner_cur.val == inner_cur.next.val:  # duplicated, pass it
                    inner_cur = inner_cur.next
                    duplicated += 1
                    continue
                else:  # next is not duplicated with current
                    if duplicated:  # previous node(s) are duplicated
                        # pass all the duplicated one
                        inner_cur = inner_cur.next  # 0->1->1->1->2->... -> 0->2
                        break
                    else:
                        break
            else:  # the last one
                if duplicated:
                    inner_cur = inner_cur.next  # 2->2->None
                else:
                    break  # 2->2->3->None

        if duplicated:
            cur = inner_cur
            pre.next = cur
            continue
        else:
            pre = cur
            cur = cur.next
    return mHead.next

```

Finally finished it!
