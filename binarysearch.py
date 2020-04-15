def binarySearch(array, search_val):
        max_index = len(array) - 1
        min_index = 0

        while min_index <= max_index:
            search_index = (max_index + min_index) // 2

            print("search index is " + str(search_index))
            print("Max index is " + str(max_index))
            print("min index is " + str(min_index))


            if search_val == array[search_index]:
                
                return search_index
            

            if search_val > array[search_index]:
                
                min_index = search_index + 1

            if search_val < array[search_index]:

                max_index = search_index - 1
        

        if min_index > max_index:
            return None


list1 = [1,3,5,7,9,11,13,15,17,19]

print(binarySearch(list1,18))
            
