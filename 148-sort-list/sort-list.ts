/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val=(val===undefined ? 0 : val)
 *         this.next=(next===undefined ? null : next)
 *     }
 * }
 */

function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;

    // Split list into two halves
    const mid = getMid(head);
    const left = head;
    const right = mid.next;
    mid.next = null;

    // Recursively sort both halves
    return merge(sortList(left), sortList(right));
}

function getMid(head: ListNode): ListNode {
    let slow = head;
    let fast = head.next;

    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    return slow;
}

function merge(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let current = dummy;

    while (l1 && l2) {
        if (l1.val <= l2.val) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }

    current.next = l1 || l2;
    return dummy.next;
}