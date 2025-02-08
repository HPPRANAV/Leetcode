func twoSum(nums []int, target int) []int {
    hash_set := make(map[int]int)
    //res := []int{}
    for i, num := range nums{
        diff := target - num
        value, ok := hash_set[diff]
        if ok{
           return []int{value, i}
        }
        hash_set[num] = i
    }
    return []int{}
}