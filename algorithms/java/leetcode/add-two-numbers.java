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
import java.math.BigInteger;

class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode currentNodeA = l1;
        ListNode currentNodeB = l2;
        BigInteger digit = BigInteger.valueOf(1);
        
        BigInteger a = digit.multiply(
            BigInteger.valueOf(l1.val)
        );
        BigInteger b = digit.multiply(
            BigInteger.valueOf(l2.val)
        );
        
        while(currentNodeA.next != null || currentNodeB.next != null) {
            digit = digit.multiply(
                BigInteger.valueOf(10)
            );
            
            if(currentNodeA.next != null) {
                currentNodeA = currentNodeA.next;
                a = a.add(
                    digit.multiply(
                        BigInteger.valueOf(
                            currentNodeA.val
                        )
                    )
                );            
            }
            
            if(currentNodeB.next != null) {
                currentNodeB = currentNodeB.next;
                b = b.add(
                    digit.multiply(
                        BigInteger.valueOf(
                            currentNodeB.val
                        )
                    )
                );
            }
        }            

        String string = String.valueOf(a.add(b));
        ListNode start = null;
        ListNode next = null;
        ListNode temp = null;
        for(int i = string.length()-1; i >= 0; i --) {
            temp = next;
            next = new ListNode(Character.getNumericValue(string.charAt(i)));
            if(i == string.length()-1) {
                start = next;
                continue;
            }
            temp.next = next;
        }
        
        return start;
    }
}