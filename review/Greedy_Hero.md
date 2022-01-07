# Greedy Hero

> DotA is a popular computer game played between two teams, each of which consists of $N$ players. Each player independently controls a powerful character, known as a "hero". When playing DotA with god-like rivals and pig-like team members, you have to face an embarrassing situation: all your teammates are killed, and you have to fight with all other N rivals alone.
>
> Let's model this problem. There are two key attributes for the heroes in the game, health point (HP) and damage per shot (DPS). Assume your hero has infinite HP and units DPS (DPS=1), but others' heroes have limited HP ($1 \le HP \le 1000$) and fixed DPS ($1 \le DPS \le 1000$). In order to futher simplify the problem, we assume the game is turn-based, but not real-time. In each round, you can attack one rival, so his HP will decrease by your unit DPS. At the same time, your HP will decrease by the summation of DPS attacked every lived rival. If one hero's HP fall equal to (or below) zero, he will die forever.
>
> For example, there are 2 rivals. Rival A has 1 HP and 100 DPS, rival B has 100 HP and 1 DPS. You attack rival A in the first round, then you will get a 101 HP loss (attacked by both A and B). As A died in the first round, you just need to fight with B in the following rounds. After another 100 rounds, B die and you win with 100 HP loss. So the summation of HP loss is 201 under this strategy.
>
> Although your hero is undefeated (with infinite HP), please give your algorithm to get the best strategy to kill all the enemy heroes with minimum HP loss (6 marks), prove the correctness (4 marks) and analyze the complexity of your algorithm (2 marks).

> DotA是一款很火的双阵营对抗游戏，每个阵营共有N名玩家。每个玩家都可以控制一个强大的单位，称为“英雄”。当在游戏中碰到如同神一般的敌人和猪一样的队友时，常会面临一个尴尬局面：队友全都阵亡了，你需要“一夫当关”对抗N名敌人。
>
> 让我们对这个问题建模。“英雄”有两种关键属性——生命值（HP）和伤害输出（DPS）。假设你的英雄有无限的HP和单位DPS（DPS=1），但其他的英雄仅有有限的HP（$1 \le HP \le 1000$）和固定的DPS（$1 \le DPS \le 1000$）。为了进一步简化问题，我们假设游戏不是实时的，而是采用回合制模式。在每一回合，你可以攻击一名敌人，其HP会减少等同于你的DPS的值。同时，你的HP会减少等同于敌方存活英雄的全部DPS总和的值。当一个英雄的HP降低至（或小于）0时，其永久阵亡。
>
> 举个例子，现有2个敌人，敌人A有1点HP和100点DPS，敌人B有100点HP和1点DPS。在第一回合，你攻击A，然后你受到101点伤害（被A和B同时攻击）（受到X点伤害等价于HP，即生命值减少X点）。于是A在第一回合便阵亡了，此后，你只需要同B单挑。则在这种策略下，最终所受的总伤害为201点。
>
> 虽然说你的英雄不会阵亡（因为拥有无限的HP），但仍请设计一个最优策略，使得在打败所有敌人的情况下，损失的HP尽量少。证明算法的正确性（4分）且分析算法的复杂度（2分）。

* **输入**：敌人的生命值（HP）$H$（任一元素$x$均满足$1 \le x \le 1000$），和伤害输出（DPS）$D$（任一元素$x$均满足$1 \le x \le 1000$）。
* **输出**：损失的HP值$L$。

---

* **思路**：要求损失的HP尽量低，必然要持续对同一个敌人进行攻击，直至该敌人失去所有HP，即阵亡后，再转移目标。于是问题简化为：应该如何确定攻击对象的顺序？直觉上应该优先攻击DPS最高的敌人，因为这样的话，后续的总DPS值就会降低，即我方英雄所承受的伤害降低。但考虑极端情况：如果DPS最高的敌人HP也非常多，但有的敌人DPS低但HP很少，是否应该先攻击后者呢？

  现假设有两个敌人A和B，其HP分别为$H_A$和$H_B$，其DPS分别为$D_A$和$D_B$，$H_A>H_B$，$D_A<D_B$。由于我方英雄的DPS只有1，所以总回合数为$H_A+H_B$。如果先攻击A，那么损失的HP为：$L_1=H_AD_A+(H_A+H_B)D_B=H_AD_A+H_AD_B+H_BD_B$；如果先攻击B，那么损失的HP为：$L_2=(H_A+H_B)D_A+H_BD_B=H_AD_A+H_BD_A+H_BD_B$。令$L_1<L_2$，得$H_AD_B<H_BD_A$，将不等式移项后得：$\frac{D_A}{H_A}>\frac{D_B}{H_B}$。可得：应优先攻击DPS与HP的比值较高的英雄。

* **算法**：遍历$H$和$D$，计算所有敌方英雄的DPS与HP的比值并用列表存储，并对该列表进行排序（假设升序），然后循环将列表中最尾部的元素剔除，并计算击败该英雄所承受的伤害，将伤害进行累加。当列表为空时，输出总伤害。

* **正确性证明**：由于我方英雄的DPS是确定值，为1，因此打败所有敌人的回合总数是确定的，即所有敌人的HP之和。题目要求在打败所有敌人的情况下，损失的HP最少，这就意味着需要对一个敌人进行持续的攻击，直到其阵亡后，再转移目标。如果不采取这一策略，如在敌人A还剩下1点HP时转而攻击敌人B，那么当前回合就会受到A的攻击，而这是可以通过直接攻击敌人A令其阵亡避免的。采用这一策略后，需要确定攻击对象的顺序，即按照怎样的顺序攻击敌方英雄。优先攻击DPS与HP的比值最大的敌方英雄是贪心策略，而该策略为最优策略是可被证明的。

  **贪心选择的正确性**：假设当前有$n$个敌人，分别为$R_1,R_2,...R_n$，他们的生命值分别为$H_1,H_2,...H_n$，DPS分别为$D_1,D_2,...D_n$。$m_i=\frac{D_i}{H_i}$，$1 \le i \le n$，而$m_t=max(m_1,m_2,...m_n)$。不妨设$R_u$，$1 \le u \le n$，讨论攻击$R_t$还是攻击$R_u$，最终我方英雄失去的生命值$L$更少。当讨论$R_t$和$R_u$时，其他英雄的伤害都是相等的，所以不必关心。如果先攻击$R_t$，则$L_t=H_tD_t+(H_t+H_u)D_u$；若先攻击$R_u$，则$L_u=H_uD_u+(H_t+H_u)D_t$。则有：
  $$
  L_t-L_u=H_tD_u-H_uD_t=H_tH_u(\frac{D_u}{H_u}-\frac{D_t}{H_t})=H_tH_u(m_u-m_t)<0
  $$
  故$L_t<L_u$恒成立。

* **复杂度**：

  * **时间复杂度**：进行一次排序，时间复杂度为$O(NlogN)$；随后的计算的时间复杂度为$O(N)$，故总时间复杂度为$O(NlogN)$。
  * **空间复杂度**：开辟了一个长度为$N$列表，没有使用递归，空间复杂度为$O(N)$。

* **伪代码**：

  ~~~pseudocode
  Function Greedy_Hero(N, H, D):
  	/* 计算 DPS / HP 的值并存储 */
  	M = [];	/* M 为空数组 */
  	for i = 0 to N-1 do
  		M.append(D[i] / H[i]);
  	end for
  	
  	/* 初始化索引数组 */
  	order = [0, 1, ..., N-1];
  	
  	/* 对 M 进行排序，同时对 order 进行同样的操作 */
  	Sort M and do the same operation for order;
  	
  	DPS_sum = sum(D); 	/* 计算敌人的总 DPS */
      L = 0;  		   /* 初始化我方英雄损失的 HP 值 */
      for i = 0 to N-1 do
      	j = order[N - i - 1];  	/* 当前攻击的敌人的索引 */
          L += DPS_sum * H[j]; 	/* 击败该敌人过程中损失的 HP 值 */
          DPS_sum -= D[j];  		/* 减去阵亡英雄的 DPS */
      end for
         
  	return L;	/* 返回总共失去的 HP 值 */
  ~~~

* **Python3 代码**：

  ~~~python
  def greedy_hero(N, H, D):
      """
      :param N: 敌方英雄总数
      :param H: 敌方英雄的生命值（HP）
      :param D: 敌方英雄的伤害输出（DPS）
      :return: 我方英雄损失的 HP 值
      """
      # 计算 DPS / HP 的值并存储
      M = [D[i] / H[i] for i in range(N)]
  
      # 对 M 进行升序排序，order 为对应的英雄索引
      order = [i for i in range(N)]  # [0, 1, ..., N-1]
      order = [x for _, x in sorted(zip(M, order))]
  
      DPS_sum = sum(D)  # 敌人的总 DPS
      L = 0  # 我方英雄损失的 HP 值
      for i in range(N):
          j = order[N - i - 1]  # 当前攻击的敌人
          L += DPS_sum * H[j]  # 击败该敌人过程中损失的 HP 值
          DPS_sum -= D[j]  # 减去阵亡英雄的 DPS
  
      return L
  ~~~

  
