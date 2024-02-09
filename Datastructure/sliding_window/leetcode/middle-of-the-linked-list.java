/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
         if(head.next == null){
            return head;
        }

        ListNode temp = head;
        int count = 1;
        while(temp.next != null){
            count++;
            temp = temp.next;
        }

        temp = head;
        int count1 = 0;
        while(count1 != count/2){
            count1++;
            temp = temp.next;
        }

        return temp;
        
    }
        
    }
