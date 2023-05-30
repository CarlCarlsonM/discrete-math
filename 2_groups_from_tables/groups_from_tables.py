'''
Function to determine if a matrix is a square matrix
Input:
 * a 2D array -> matrix
Output:
 * a boolean (are all the lengths of all rows and cols the same?)
'''
def is_square_matrix(matrix):    
    for row in range(len(matrix)):
        if (len(matrix) != len(matrix[row])):
            return False
    
    return True

'''
Function to transpose a matrix (assuming it is square)
Input:
 * a 2D array -> matrix
Output:
 * a transposed 2D array (the input matrix flipped over its diagonal)
'''
def transpose_square_matrix(matrix):
    transpose = []
    
    for i in range(len(matrix)):
        transpose.append([])
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])
    
    return transpose

'''
Function to determine if a element from an array is within the domain (table_set)
Input: 
 * an element from the 2D array -> element
 * an array (the domain) -> table_set
Output:
 * a boolean (is the element within the domain?)
'''
def is_element_in_table_set(element, table_set):
    for index in range(len(table_set)):
        if (element == table_set[index]):
            return True
    
    return False

'''
Function to determine if a given row has all unique items (and if all items are within the table set)
Input:
 * an array (a row of a 2D array) -> row
 * an array (the domain) -> table_set
Output:
 * a boolean (does it have unique items and within the table set?)
'''
def does_row_have_unique_items_and_within_table_set(row, table_set):    
    for current_index in range(len(row) - 1):
        if not is_element_in_table_set(row[current_index], table_set):
                return False
        
        comparing_index = current_index + 1
        
        while (comparing_index < len(row)):
            if (row[current_index] == row[comparing_index]):
                return False
            if not is_element_in_table_set(row[comparing_index], table_set):
                return False
             
            comparing_index = comparing_index + 1
    
    return True

'''
Function to determine if an array is a latin square
Input:
 * a 2D array -> matrix
 * an array (the domain) -> table_set
Output:
 * a boolean (is it a latin square?)
'''
def is_latin_square(matrix, table_set):
    if (is_square_matrix(matrix)):
        transpose = transpose_square_matrix(matrix)
        
        for row in range(len(matrix)):
            if not does_row_have_unique_items_and_within_table_set(matrix[row], table_set):
                return False
                break
            if not does_row_have_unique_items_and_within_table_set(transpose[row], table_set):
                return False
                break
    else:
        return False
    
    return True

'''
Function to determine if the table is closed under operation
Input: 
 * a 2D array -> multiplication_table
 * an array (the domain) -> table_set
Output:
 * a boolean (is the table closed under operation?)
'''
def is_the_table_closed_under_operation(multiplication_table, table_set):
    for i in range(len(multiplication_table)):
        for j in range(len(multiplication_table)):
            if not is_element_in_table_set(multiplication_table[i][j], table_set):
                return False
    
    return True

'''
Function to determine if there is the identity element in a given row
Input: 
 * an array (a row of a 2D array) -> row
 * an array (the domain) -> table_set
 * an integer (the current row of the multiplcation table where we are) -> current_index
Output:
 * a specific element of the array (the identity element of the row)
'''
def get_the_identity_element_in_row(row, table_set, current_index):
    for index in range(len(row)):
        if (row[index] == table_set[current_index]):
            return table_set[index]
    
    return None

'''
Function to determine if the identity element is in each row of the multiplication table
Input: 
 * a 2D array -> multiplication_table
 * an array (the domain) -> table_set
Output:
 * a specific element of the 2D array (the identity element of the whole table, it is unique)
'''
def get_the_identity_element_in_table(multiplication_table, table_set):
    identity_element = None
    
    for index in range(len(multiplication_table)):
        if (index == 0):
            identity_element = get_the_identity_element_in_row(multiplication_table[index], table_set, index)
        if (identity_element != get_the_identity_element_in_row(multiplication_table[index], table_set, index)):
            return None
    
    return identity_element

'''
Function to determine if the identity element exisits in the table
Input: 
 * a 2D array -> multiplication_table
 * an array (the domain) -> table_set
Output:
 * a boolean (the identity element exists?)
'''
def is_there_the_identity_element_in_table(multiplication_table, table_set):
    return (get_the_identity_element_in_table(multiplication_table, table_set) != None)

'''
Function to get the inverse element of each row
Input: 
 * an array (a row of a 2D array) -> row
 * an array (the domain) -> table_set
 * an element (previously obtained) -> identity_element
Output:
 * an element (the inverse)
'''
def get_the_inverse_element_in_row(row, table_set, identity_element):
    for index in range(len(row)):
        if (row[index] == identity_element):
            return table_set[index]
    
    return None

'''
Function to determine if each row on the table has an inverse
Input: 
 * a 2D array -> multiplication_table
 * an array (the domain) -> table_set
Output:
 * a boolean (do we have an inverse element on each row?)
'''
def is_there_the_inverse_element_in_table(multiplication_table, table_set):
    identity_element = get_the_identity_element_in_table(multiplication_table, table_set)
    
    for index in range(len(multiplication_table)):
        inverse = get_the_inverse_element_in_row(multiplication_table[index], table_set, identity_element)
        if (get_the_inverse_element_in_row(multiplication_table[index], table_set, identity_element) == None):
            return False
    
    return True

'''
Function to get the index of a given element in the domain array
Input: 
 * an element from the 2D array -> element
 * an array (the domain) -> table_set
Output:
 * a number (the index of the domain array where the element is)
'''
def get_index_of_element_in_table_set(element, table_set):
    for index in range(len(table_set)):
        if (element == table_set[index]):
            return index

'''
Function to determine if there is asociativity given the multiplication table
Input: 
 * a 2D array -> multiplication_table
 * an array (the domain) -> table_set
Output:
 * a boolean (is the multiplication_table asociative)
'''
def is_the_operation_asociative(multiplication_table, table_set):
    for i in range(len(multiplication_table)):
        for j in range(len(multiplication_table)):
            for k in range(len(multiplication_table)):
                x = get_index_of_element_in_table_set(multiplication_table[i][j], table_set)
                y = get_index_of_element_in_table_set(multiplication_table[j][k], table_set)
                
                if (multiplication_table[x][k] != multiplication_table[i][y]):
                    return False
                    
    return True

'''
Function to determine if the a given multiplication table qualifies as a group 
(we call several methods already defined)
Input: 
 * a 2D array -> multiplication_table
 * an array (the domain) -> table_set
Output:
 * a boolean (is the table a group?)
'''
def is_matrix_a_group(multiplication_table, table_set):
    if (is_square_matrix(multiplication_table)):
        if (is_the_table_closed_under_operation(multiplication_table, table_set) and
            is_there_the_identity_element_in_table(multiplication_table, table_set) and
            is_there_the_inverse_element_in_table(multiplication_table, table_set) and
            is_the_operation_asociative(multiplication_table, table_set)):
                        return True
    
    return False

'''
Function to print any given 2D array
'''
def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])

'''
Function to print the basic info about this homework
'''
def print_program_info():
    print("--------------------------------------------------")
    print("Python homework:")
    print("Detect groups from multiplication tables")
    print("--------------------------------------------------")
    print("Author:")
    print("Carlos Arturo Murcia Andrade")
    print("--------------------------------------------------")
    print("\n")
    
    print("--------------------------------------------------")
    print("Homework description:")
    print("We will determine if sample matrices")
    print("(loaded to this program) are considered")
    print("groups or not.")
    print("We will also determine if those matrices")
    print("are latin squares or not")
    print("--------------------------------------------------")
    print("\n")

'''
Function to print the results given all the samples we defined on the main methods
Input:
 * a 2D array (all the multiplication tables and corresponding domain sets) -> table_and_set_pairs
'''
def print_results(table_and_set_pairs):
    for i in range(len(table_and_set_pairs)):
        print("--------------------------------------------------")
        print("Sample " + str(i + 1) + " of " + str(len(table_and_set_pairs)) + ":")
        print("--------------------------------------------------")
        print("Multiplication table: ")
        print_matrix(table_and_set_pairs[i][0])
        print("--------------------------------------------------")
        print("Is this matrix a square matrix?: " + str(is_square_matrix(table_and_set_pairs[i][0])))
        print("--------------------------------------------------")
        print("Is this matrix a latin square?: " + str(is_latin_square(table_and_set_pairs[i][0], table_and_set_pairs[i][1])))
        print("--------------------------------------------------")
        print("In this matrix closed under operation?: " + str(is_the_table_closed_under_operation(table_and_set_pairs[i][0], table_and_set_pairs[i][1])))
        print("--------------------------------------------------")
        print("Is there the identity element in the matrix?: " + str(is_there_the_identity_element_in_table(table_and_set_pairs[i][0], table_and_set_pairs[i][1])))
        print("--------------------------------------------------")
        print("Is there the inverse element in the matrix?: " + str(is_there_the_inverse_element_in_table(table_and_set_pairs[i][0], table_and_set_pairs[i][1])))
        print("--------------------------------------------------")
        print("Is the operation asociative?: " + str(is_the_operation_asociative(table_and_set_pairs[i][0], table_and_set_pairs[i][1])))
        print("--------------------------------------------------")
        print("Does this matrix represent a group?: " + str(is_matrix_a_group(table_and_set_pairs[i][0], table_and_set_pairs[i][1])))
        print("--------------------------------------------------")
        print("\n")

'''
Main method
'''
def main():
    sample_table_1 = [["g1", "g3", "g4", "g5", "g2"],
                       ["g3", "g2", "g5", "g1", "g4"],
                       ["g4", "g5", "g3", "g2", "g1"],
                       ["g5", "g1", "g2", "g4", "g3"],
                       ["g2", "g4", "g1", "g3", "g5"]]

    table_set_1 = ["g1", "g2", "g3", "g4", "g5"]

    sample_table_2 = [["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8"],
                       ["g2", "g3", "g4", "g1", "g7", "g8", "g6", "g5"],
                       ["g3", "g4", "g1", "g2", "g6", "g5", "g8", "g7"],
                       ["g4", "g1", "g2", "g3", "g8", "g7", "g5", "g6"],
                       ["g5", "g8", "g6", "g7", "g1", "g3", "g4", "g2"],
                       ["g6", "g7", "g5", "g8", "g3", "g1", "g2", "g4"],
                       ["g7", "g5", "g8", "g6", "g2", "g4", "g1", "g3"],
                       ["g8", "g6", "g7", "g5", "g4", "g2", "g3", "g1"]]

    table_set_2 = ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8"]
    
    sample_table_3 = [["a", "b", "c", "d"],
                       ["c", "d", "d", "d"],
                       ["a", "b", "d", "c"],
                       ["d", "a", "c", "d"]]

    table_set_3 = ["a", "b", "c", "d"]
    
    sample_table_4 = [["e", "a", "b", "c"],
                       ["a", "e", "c", "b"],
                       ["b", "c", "e", "a"],
                       ["c", "b", "a", "e"]]

    table_set_4 = ["e", "a", "b", "c"]
    
    # Representation of symmetries of a regular hexagon
    sample_table_5 = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
                      ["b", "c", "d", "e", "f", "a", "h", "i", "j", "k", "l", "g"],
                      ["c", "d", "e", "f", "a", "b", "i", "j", "k", "l", "g", "h"],
                      ["d", "e", "f", "a", "b", "c", "j", "k", "l", "g", "h", "i"],
                      ["e", "f", "a", "b", "c", "d", "k", "l", "g", "h", "i", "j"],
                      ["f", "a", "b", "c", "d", "e", "l", "g", "h", "i", "j", "k"],
                      ["g", "h", "i", "j", "k", "l", "a", "b", "c", "d", "e", "f"],
                      ["h", "i", "j", "k", "l", "g", "b", "c", "d", "e", "f", "a"],
                      ["i", "j", "k", "l", "g", "h", "c", "d", "e", "f", "a", "b"],
                      ["j", "k", "l", "g", "h", "i", "d", "e", "f", "a", "b", "c"],
                      ["k", "l", "g", "h", "i", "j", "e", "f", "a", "b", "c", "d"],
                      ["l", "g", "h", "i", "j", "k", "f", "a", "b", "c", "d", "e"]]

    # Representation of the set of all possible rotations and reflections of a regular hexagon
    table_set_5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

    # Representation of the operations between S2 x S3
    sample_table_6 = [['a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'g', 'h', 'k', 'l'],
                      ['b', 'a', 'd', 'c', 'f', 'e', 'j', 'i', 'h', 'g', 'l', 'k'],
                      ['c', 'd', 'a', 'b', 'i', 'j', 'e', 'f', 'k', 'l', 'g', 'h'],
                      ['d', 'c', 'b', 'a', 'j', 'i', 'f', 'e', 'l', 'k', 'h', 'g'],
                      ['e', 'f', 'g', 'h', 'a', 'b', 'k', 'l', 'c', 'd', 'i', 'j'],
                      ['f', 'e', 'h', 'g', 'b', 'a', 'l', 'k', 'd', 'c', 'j', 'i'],
                      ['g', 'h', 'e', 'f', 'k', 'l', 'a', 'b', 'i', 'j', 'c', 'd'],
                      ['h', 'g', 'f', 'e', 'l', 'k', 'b', 'a', 'j', 'i', 'd', 'c'],
                      ['i', 'j', 'k', 'l', 'c', 'd', 'g', 'h', 'a', 'b', 'e', 'f'],
                      ['j', 'i', 'l', 'k', 'd', 'c', 'h', 'g', 'b', 'a', 'f', 'e'],
                      ['k', 'l', 'i', 'j', 'g', 'h', 'c', 'd', 'e', 'f', 'a', 'b'],
                      ['l', 'k', 'j', 'i', 'h', 'g', 'd', 'c', 'f', 'e', 'b', 'a']]

    # Representation of the set of all possible permutation of S2 x S3
    table_set_6 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    
    table_and_set_pairs = []
    table_and_set_pairs.append([sample_table_1, table_set_1])
    table_and_set_pairs.append([sample_table_2, table_set_2])
    table_and_set_pairs.append([sample_table_3, table_set_3])
    table_and_set_pairs.append([sample_table_4, table_set_4])
    table_and_set_pairs.append([sample_table_5, table_set_5])
    
    print_program_info()
    print_results(table_and_set_pairs)
    
if __name__=="__main__":
    main()