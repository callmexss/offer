import offerhelper
from offerhelper import ListNode


class Solution:
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
                        # print("inner_cur:", inner_cur.val)
                        inner_cur = inner_cur.next
                        duplicated += 1
                        continue
                    else:  # not duplicated
                        if duplicated:
                            # print("inner_cur:", inner_cur.val)
                            inner_cur = inner_cur.next
                            break
                        else:
                            # print("inner_cur:", inner_cur.val)
                            break
                else:  # the last one
                    if duplicated:
                        inner_cur = inner_cur.next  # 2->2->None
                    else:
                        break  # 2->2->3->None

            # if inner_cur:
                # print("out_cur:", inner_cur.val)

            if duplicated:
                cur = inner_cur
                pre.next = cur
                continue
            else:
                pre = cur
                cur = cur.next
        return mHead.next




def test(solution):
    li = offerhelper.gen_random_list(100, 0, 1000)
    li.sort()
    testcases = [
             ([], []),
             ([1], [1]),
             ([1, 1, 1], []),
             ([1, 2, 3], [1, 2, 3]),
             ([4, 4, 5], [5]),
             ([2, 4, 4, 5], [2, 5]),
             ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
             (li, [x for x in li if li.count(x) == 1])
            ]

    for testcase in testcases:
        in_list = testcase[0]
        out_list = testcase[1]
        list_node = offerhelper.create_linked_list(in_list)
        head = solution.deleteDuplication(list_node)
        ret = offerhelper.convert_linked_list_to_list(head)
        # print(ret, out_list)
        assert ret == out_list, f"{testcase}"

    print("All testcases passed.")


if __name__ == '__main__':
    test(Solution())

