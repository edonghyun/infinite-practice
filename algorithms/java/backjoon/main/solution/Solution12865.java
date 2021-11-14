package main.solution;

import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

import main.solution.Solution;
/*

이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 

세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 

해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 

아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 

준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 

두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

*/

public class Solution12865 extends Solution {
    public static void solve(List<String> testText) throws Exception {
        class Item {
            public Integer weight;
            public Integer value;

            public Item(Integer weight, Integer value) {
                this.weight = weight;
                this.value = value;
            }

            public String toString() {
                return String.format("weight: %s value: %s", this.weight, this.value);
            }
        }

        Integer itemNumber = -1;
        Integer limitWeight = -1;

        List<Item> itemList = new ArrayList<Item>();

        for (int i = 0; i < testText.size(); i++) {
            List<Integer> line = List.of(testText.get(i).split(" ")).stream().map(s -> Integer.parseInt(s))
                    .collect(Collectors.toList());
            if (i == 0) {
                itemNumber = line.get(0);
                limitWeight = line.get(1);
                itemList.add(new Item(0, 0));
            } else {
                itemList.add(new Item(line.get(0), line.get(1)));
            }
        }

        int[][] dp = new int[itemNumber + 1][limitWeight + 1];
        for (int i = 1; i <= itemNumber; i++) {
            for (int j = 1; j <= limitWeight; j++) {
                int weight = itemList.get(i).weight;
                int without = dp[i - 1][j];
                if (j - weight < 0) {
                    dp[i][j] = without;
                    continue;
                }
                int with = dp[i - 1][j - weight] + itemList.get(i).value;
                dp[i][j] = Math.max(without, with);
            }
        }

        System.out.println(dp);
        System.out.println(dp[itemNumber][limitWeight]);

        System.out.println(String.format("itemNumber: %s limitWeight: %s", itemNumber, limitWeight));
        System.out.println(itemList);
    }
}
