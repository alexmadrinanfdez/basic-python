def permute(nums):
        return [[n] + p
            for i, n in enumerate(nums)
            for p in permute(nums[:i] + nums[i+1:])] or [[]]

if __name__ == "__main__":
    print(permute(list(range(3))))