N = int(input())
lens = list(map(int, input().split()))

maximum = max(lens)
lens.remove(maximum)
sum_no_max = sum(lens)


if maximum > sum_no_max:
    print(maximum-sum_no_max)
elif maximum <= sum_no_max:
    print(sum_no_max+maximum)




