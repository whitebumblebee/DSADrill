# Subarray Problems

Below is a structured roadmap for tackling subarray problems in DSA, moving from fundamentals to more advanced patterns. Read through each section carefully, understand the core idea and techniques, and then attempt representative problems on your own. As you progress, try to recognize which pattern applies and how to optimize a brute-force approach step by step.

---

## 1. Understand “Subarray” vs. “Subsequence” vs. “Subset”

Before diving into algorithms, be crystal-clear on definitions:

- **Subarray:** A contiguous slice of an array. For example, in `[1, 2, 3, 4]`, `[2, 3]` is a subarray but `[1, 3]` is not (because it skips 2).
- **Subsequence:** Not necessarily contiguous—obtained by deleting zero or more elements without reordering. E.g., `[1, 3, 4]` is a subsequence of `[1, 2, 3, 4]`.
- **Subset:** Any selection of elements, regardless of order or contiguity.

All “subarray problems” require contiguous segments. Practically, this contiguity constraint unlocks certain array-prefix patterns, sliding windows, or divide-and-conquer approaches.

---

## 2. Basic Brute-Force and Prefix Sum

### 2.1 Brute-Force Enumeration (O(n³) → O(n²))

1. **Naïve idea:** To consider every subarray, use two nested loops (start = 0..n−1, end = start..n−1) and then a third loop to compute sum/other property of `arr[start..end]`. That’s O(n³) total.
2. **Optimize to O(n²):** Precompute a prefix-sum array `P` where

   ```
   P[i] = arr[0] + arr[1] + … + arr[i−1],   (P[0] = 0)
   ```

   Then the sum of any subarray `[L..R]` is `P[R+1] − P[L]`. With two nested loops for all (L, R), you compute sums in O(1) each → O(n²).

**When to use:** If n ≲ 10⁴ and you only need sums or simple checks. Getting comfortable with prefix sums is crucial—even more complex approaches often generalize from prefix-sum ideas.

### 2.2 Practice Problems

- Compute the sum of every subarray and print them.
- Given an array, find the maximum sum among all subarrays (still brute-force).
- Count how many subarrays have sum = k (first approach: O(n²) with prefix sums).

---

## 3. The “Maximum Subarray” (Kadane’s Algorithm)

The classic “maximum sum contiguous subarray” problem appears everywhere.

1. **Problem statement:** Given `arr[]`, find a contiguous nonempty subarray with the largest sum.
2. **Brute-force:** O(n²) with prefix sums.
3. **Optimal (Kadane’s):**

   - Maintain two variables: `current_max` (max subarray ending at the current index) and `global_max` (best overall so far).
   - For each `i` from 0..n−1:

     ```
     current_max = max(arr[i], current_max + arr[i])
     global_max = max(global_max, current_max)
     ```

   - Answer = `global_max`.

4. **Why it works:** If the subarray ending at i−1 has negative sum, it’s better to start fresh at `i`. If it’s positive, extend it.

**Time Complexity:** O(n)
**Memory:** O(1)

### 3.1 Variants to Try

- “Maximum subarray” when **all numbers are negative**: Kadane’s still works if initialized properly (e.g., `global_max = arr[0]`).
- “Minimum sum subarray” (just invert signs or adjust comparisons).
- “Maximum subarray with length at most K” (slightly more complex—maintain a deque of prefix minima).
- “Maximum subarray with at least K length” (prefix-sum + data structure or sliding window approach).

---

## 4. Sliding Window & Two-Pointer Patterns

Sliding window techniques shine when the array contains only nonnegative values (or when tracking counts/frequencies rather than sums). Most sliding-window subarray problems have the form:

> “Find the longest/shortest/any subarray that satisfies condition C (sum ≤ X, sum ≥ X, at most K distinct, etc.)”

### 4.1 Fixed-Size Window

- **When the subarray length is fixed (say K)**: Use a window of size K, maintain its sum (add new element, subtract departing element) → O(n).
- **Example:** Find all subarrays of length K with sum > S.

### 4.2 Variable-Size Window (Expand/Contract)

The general pattern to find the **smallest or largest** subarray satisfying a sum or count constraint:

1. Initialize `left = 0`, `current_sum = 0` (or a frequency map, `count = 0` for distinct elements, etc.).
2. For `right` from `0` to `n−1`:

   - Include `arr[right]` into your window (e.g., `current_sum += arr[right]`).
   - While the window “meets or exceeds” the condition you care about, try to contract from the left:

     - Update answer (e.g., record window length or count).
     - Remove `arr[left]` from window (`current_sum -= arr[left]`), `left++`.

3. Continue until `right` reaches end.

**Key points:**

- Works best when the property is monotonic as you expand/contract (e.g., sum increasing when adding +ve numbers).
- If array can have negatives, sliding window on sums alone becomes tricky—then you often fall back to prefix sums + data structures (see next section).

### 4.3 Typical Sliding-Window Subarray Questions

1. **Smallest subarray with sum ≥ S** (all positives):

   - Expand `right` until sum ≥ S, then shrink `left` while still ≥ S; track min length.

2. **Longest subarray with sum ≤ S** (all positives):

   - Expand until sum > S, then shrink until sum ≤ S; track max length.

3. **Longest subarray with at most K distinct elements:**

   - Use a frequency map: expand until distinct > K, then shrink.

4. **Count subarrays with sum ≤ S (positives only):**

   - Maintain a running window; every time you add a new right, all subarrays ending at `right` and starting ≥ `left` are valid.

5. **Maximum sum subarray of size at most K**:

   - Either sliding window (if all positives) or prefix sums + min‐queue (if arbitrary numbers).

---

## 5. Hash-Map + Prefix Sum for “Sum = K” Variants

When the array can contain negatives, the simple sliding window breaks. Instead, use a **prefix-sum + hash map** to record how many times a certain prefix sum has appeared.

### 5.1 Count of Subarrays with Sum = K

**Approach:**

1. Let `prefix_sum = 0`. Create a map `mp` that maps a prefix_sum value → count of occurrences. Initialize `mp[0] = 1`.
2. Iterate `i` from 0 to n−1:

   - `prefix_sum += arr[i]`.
   - You want `prefix_sum − K` to have appeared before. If `mp[prefix_sum − K]` exists, add that count to your answer.
   - Increment `mp[prefix_sum]` by 1.

3. The final answer is how many subarrays sum exactly to K.

**Time Complexity:** O(n)
**Memory:** O(n) (for the map)

### 5.2 Longest Subarray with Sum = K

- Similar idea: You store in a map not the count of a prefix sum, but the earliest index where each prefix sum occurred.
- When you compute `prefix_sum` at index i, if `(prefix_sum − K)` has been seen at index j, the subarray `(j+1 … i)` has sum = K.
- Track `i − j` to maximize length; only store the first occurrence of any prefix value (for longest).

### 5.3 Other “Sum = K” Variants

- **Longest Zero-Sum Subarray**: Set K = 0 and use the same approach.
- **Count subarrays with sum ≤ K**: Harder—often done by sorting prefix sums and using a Fenwick Tree or Balanced BST to count how many earlier prefix sums ≥ `current_sum − K`. That becomes O(n log n).
- **Number of subarrays whose sum is divisible by K**: Mod prefix sums by K, then count pairs of equal remainders via a map.

---

## 6. Divide and Conquer / Segment Tree / BIT (Advanced Queries)

When you need to answer **many queries** about subarrays (e.g., “what’s the maximum subarray sum in range \[L, R]?”), you must preprocess with a segment tree or Binary Indexed Tree (Fenwick Tree).

### 6.1 Divide and Conquer (Offline Single Query)

- A classic “max subarray sum in an interval” can be solved in O(n) by a D\&C that computes, for each segment:

  - `total_sum` of the segment.
  - `max_prefix_sum` (best subarray starting at left edge).
  - `max_suffix_sum` (best subarray ending at right edge).
  - `max_subarray_sum` anywhere in the segment.

- To get the answer for the whole array, combine left and right halves recursively. That’s O(n log n) overall to compute once.

### 6.2 Segment Tree (Multiple Queries/Updates)

- Build a tree where each node stores the four values above (`total`, `max_pref`, `max_suf`, `max_sub`).
- **Query \[L..R]:** Combine nodes for O(log n).
- **Point Update (change arr\[i]):** Recompute along the path in O(log n).

### 6.3 Fenwick Tree / BIT

- Fenwick Tree is great for prefix‐sum queries and point updates in O(log n).
- If you only need **range sum** or **range minimum/maximum** (not subarray sum problems requiring crossing‐midpoint info), BIT suffices.
- For “maximum subarray sum” queries, you need that richer node info—Fenwick cannot handle that out of the box.

### 6.4 Practice Tasks

- Implement a segment tree that returns `max_subarray_sum` for arbitrary \[L..R] queries.
- Extend it to allow point updates (change an element).
- Compare the divide-and-conquer precomputation (O(n log n)) vs. segment tree query time (O(log n)) if you need many queries.

---

## 7. “Count/Enumerate” Subarray Problems

Beyond sums, many problems ask for counting or enumerating subarrays satisfying a certain condition (product constraints, bitwise constraints, etc.). Often, the same sliding-window or prefix-sum+map patterns adapt.

### 7.1 Count Subarrays with Product < K (All positives)

- Similar to “count subarrays with sum < K” but maintain a running `product` instead of sum. Since all elements > 0:

  1. Expand right pointer, `product *= arr[right]`.
  2. While `product ≥ K` and `left ≤ right`, divide out `arr[left]` and `left++`.
  3. All subarrays ending at `right` and starting ≥ `left` are valid; add `(right − left + 1)` to count.

### 7.2 Count Subarrays with At Most K Distinct / Exactly K Distinct

- Maintain a frequency map (`char → count`) in a sliding window:

  1. Expand `right`; increment freq of `arr[right]`.
  2. While `distinct_count > K`, decrement freq of `arr[left]`, and if freq becomes 0, `distinct_count--`; then `left++`.
  3. The number of subarrays ending at `right` with ≤ K distinct = `(right − left + 1)`.

- To get **exactly** K distinct, do `atMost(K) − atMost(K−1)`.

### 7.3 Count of Subarrays with XOR == K

- Use a prefix-xor map (similar to prefix-sum):

  1. Let `prefix_xor = 0`, and `mp[0] = 1`.
  2. For each `i`:

     ```
     prefix_xor ^= arr[i]
     desired = prefix_xor ^ K
     if desired in mp: answer += mp[desired]
     mp[prefix_xor]++
     ```

---

## 8. Two-Dimensional “Subarray” (Submatrix) Extensions

Once 1D subarray patterns are comfortable, try their 2D counterparts on matrices:

### 8.1 Maximum Sum Rectangle in a 2D Matrix

- Fix two row indices, `top` and `bottom`. For each column, compute the sum of elements between `top` and `bottom`. You collapse the 2D problem into a 1D array of column-sums and then run Kadane’s on it.
- Overall complexity: O(rows² × cols). Works if rows ≲ 200 and cols ≲ 200 (n²·m).

### 8.2 Count 2D Submatrices with Sum = K

- Similar “prefix-sum + map” extension:

  1. Fix `top` and `bottom`; collapse columns into `arr[col]` = sum over rows \[top..bottom].
  2. Now count subarrays in that 1D array summing to K via the prefix-sum–map method.

- Complexity: O(rows² × cols).

---

## 9. “Mo’s Algorithm” for Offline Frequency/Count Queries

When posed with many offline queries asking for something like “in subarray \[L..R], how many distinct numbers?” or “sum of squares in \[L..R]?”, Mo’s algorithm can compute all queries in roughly O((N + Q) × √N) by sorting queries in a specific block order and maintaining a running window, adjusting `L`/`R` one step at a time. Once you have the current window’s state (frequency map, current answer), you can update in O(1) per step.

While Mo’s algorithm is not strictly a “DSA subarray technique,” it’s often the next level once you handle dynamic queries with segment trees. Imitate this pattern if you have a large list of offline subarray queries where updates are expensive otherwise.

---

## 10. Putting It All Together: Learning Path

Below is a suggested sequence. For each step, **code the solution yourself**, test on small examples, and then try 2–3 problems of that flavor on your favorite platform (LeetCode/Codeforces/InterviewBit).

1. **Warm-up (understand contiguous)**

   - Enumerate all subarrays with three loops → compute sum.
   - Build a prefix-sum array, then rewrite with two loops → O(n²).

2. **Prefix-Sum Problems**

   - Count subarrays with sum = K (use hash map).
   - Longest/shortest subarray with sum = K (store earliest index).
   - Subarray sum divisible by K (map of remainders).
   - Longest zero-sum subarray.

3. **Kadane’s Algorithm**

   - Maximum subarray sum.
   - Variants: minimum subarray sum, maximum sum with size constraint.

4. **Sliding Window (Two Pointers)**

   - Smallest subarray with sum ≥ S (all positives).
   - Longest subarray with sum ≤ S.
   - Count subarrays with product < K (all positives).
   - Count subarrays with at most/exactly K distinct.

5. **Map + Prefix-Sum for Negative Numbers**

   - Count subarrays with sum ≤ K (using balanced BST or Fenwick).
   - Count subarrays with XOR = K.
   - Longest subarray with sum divisible by K.

6. **Divide & Conquer / Segment Tree / BIT**

   - Implement a D\&C that returns (total, max_pref, max_suf, max_sub) for max subarray.
   - Build a segment tree to answer “max subarray sum in \[L..R]” with point updates.
   - Build a Fenwick tree for range-sum queries & point updates; adapt to “count subarrays” with ≤ K (via BIT + sorting).

7. **Count/Enumerate with Frequency Constraints**

   - Subarrays with at most/exactly K distinct elements.
   - Subarrays with elements that all appear at least twice (use a sliding window + freq map).
   - Subarrays with bitwise AND/OR constraints (rare, but the pattern is to maintain a running data structure of bit counts).

8. **2D Extensions**

   - Maximum sum rectangle in a matrix (collapse to 1D + Kadane).
   - Count submatrices with sum = K.

9. **Offline Queries / Mo’s Algorithm**

   - Learn Mo’s pattern: sort queries in √N blocks, move L/R pointers, update freq array, compute current answer in O(1).
   - Practice on “distinct numbers in range” or “sum of powers in subarray” queries.

10. **Very Advanced / Contest-Style**

    - “Subarray Xor sum maximum after K flips” (bitwise + greedy).
    - “Subarray with at most K zeros—longest binary subarray” (sliding window + special handling).
    - “Maximum subarray sum with one deletion allowed” (2D Kadane variation / DP).
    - “Count subarrays where median = M” (advanced prefix and counting).
    - “Subarray problems with dynamic updates (point update + range query)”—use persistent segment tree or advanced data structures.

---

## 11. Tips for Problem-Solving

1. **Pattern Recognition:**

   - If the problem asks for “maximum subarray sum,” immediately think Kadane’s.
   - If it’s “count subarrays with sum = K” and negatives appear, think prefix-sum + hash map.
   - If it’s “longest/shortest subarray with sum constraint (all positive),” sliding window likely works.

2. **Start Brute-Force (Conceptually):**

   - Write down the O(n²) prefix-sum approach. Understand its bottleneck.
   - Then ask: “Can I replace the O(n²) enumeration with (a) O(n)? (b) O(n log n) + data structure?”

3. **Edge Cases to Watch:**

   - Negative numbers break typical sliding-window sum techniques. Whenever you see negatives, pivot to prefix-sum + map or segment tree.
   - All numbers negative/zero—Kadane’s must be initialized carefully.
   - Arrays of length 0 or 1—you should handle trivial edge cases.

4. **Complexity Goals:**

   - If n ≲ 10⁴, an O(n²) solution might still pass (depending on time limits).
   - For n ≳ 10⁵, aim for O(n), O(n log n), or O(n√n) (Mo’s).
   - Always check input constraints—if 2D is involved (n × m), ensure n·m² or n²·m we can handle.

5. **Coding Practices:**

   - Modularize: Write small helper functions like `countSubarraysWithSumK(arr, K)` or `maxSubarray(arr)` and test them independently.
   - Carefully handle prefix-sum array indices (off-by-one errors).
   - When using hash maps, always remember to initialize the map with the base case (`mp[0] = 1` for sum-K counts, or store index `−1` for prefix 0 when finding longest).

6. **Debugging:**

   - Print intermediate prefix sums on small arrays to ensure they’re computed correctly.
   - For sliding window, track `left`, `right`, and `current_sum` or `freq_map` as you expand/contract on a simple example like `[2, 1, 5, 2, 3, 2]` for sum ≥ 7.

---

## 12. Suggested Practice Progression

Below is a non-exhaustive list of problem “flavors.” After reading each section above, pick a few problems of that flavor. (Platform-agnostic names; on LeetCode/JDoodle/InterviewBit/etc. you can search these titles.)

1. **Prefix-Sum Basics**

   - “Subarray Sum Equals K”
   - “Longest Zero-Sum Subarray”
   - “Count Subarrays with Sum Divisible by K”

2. **Kadane’s/Max Subarray**

   - “Maximum Subarray”
   - “Maximum Product Subarray” (slightly different twist—track max/min ending here).
   - “Best Time to Buy and Sell Stock” (variation: difference array, then Kadane’s)

3. **Sliding-Window (All Positive)**

   - “Minimum Size Subarray Sum”
   - “Count Number of Nice Subarrays” (at most K odd numbers—two pointers + freq)
   - “Subarray Product Less Than K”

4. **At Most/Exactly K Distinct**

   - “Subarrays with K Different Integers”
   - “Longest Substring with At Most K Distinct Characters” (string but same pattern)
   - “Count Good Subarrays” (at most K distinct)

5. **2D Subarray**

   - “Max Sum Rectangle in a 2D Matrix”
   - “Count Submatrices With Sum Exactly Target”

6. **Dynamic Queries / Segment Tree**

   - “Range Maximum Query”
   - “Range Add, Range Max Subarray Query” (harder)
   - “Dynamic Range Sum Queries” (Fenwick tree)

7. **Mo’s Algorithm Exercises**

   - “DQUERY” on SPOJ (distinct in \[L..R])
   - “Powerful Array” on Codeforces (sum of `cnt[v]² × v` in a range)
   - “Subarray Queries” variants in offline mode

---

## 13. Final Advice

- **Work in Small Steps:** For each new technique, code a minimal prototype on a tiny, handcrafted input.
- **Visualize:** Draw the current window or prefix sums on paper. Highlight how left/right moves or how prefix sums map to counts.
- **Keep a Cheat-Sheet of Patterns:** Whenever you finish a problem, note the pattern—e.g., “1D maximum subarray → Kadane’s,” “Count sum = K with negatives → prefix-sum + map.” Gradually, you’ll recognize patterns faster.
- **Time Yourself:** When practicing under interview conditions, set a timer (e.g., 30 minutes) to choose a strategy, code, and debug a subarray problem.
- **After Solving, Reflect:** “Why did this approach work? What if constraints changed (e.g., negatives introduced)? Would sliding window still apply, or would I need a hash map?”

By following the above roadmap—from brute-force and prefix sums → Kadane’s → sliding window → hash-map tricks → segment trees → Mo’s—you’ll build a solid foundation in subarray problems. Good luck with your practice!
