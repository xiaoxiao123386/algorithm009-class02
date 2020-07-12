# 学习笔记

## 冒泡排序

```
def bubbleSort(list):
	n = len(list)
	for i in range(n-1):
		for j in range(n-i-1):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list
```



## 选择排序

```
def selectionSort(list):
	n = len(list)
	tmp = 0
	for i in range(n-1):
		minIndex = i
		for j in range(i+1, n):
			if list[j] < list[minIndex]:
				minIndex = j
		list[i], list[minIndex] = list[minIndex], list[i]
	return list
```



## 插入排序

```
def insertionSort(list):
	n = len(list)
	for i in range(n):
		preIndex = i - 1
		current = list[i]
		while preIndex >= 0 and list[preIndex] > current:
			list[preIndex + 1] = list[preIndex]
			preIndex -= 1
		list[preIndex + 1] = current
	return list
```



