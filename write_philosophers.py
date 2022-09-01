# This program writes three lines of data to a file
def main():
# Open  a file names philosophers.txt
    outfile = open('philosophers.txt', 'w')

# Write the names of three philosophers to the file - 
# John Locke, David Hume, and Edmund Burke
    outfile.write('John Locke\nDavid Hume\nEdmund Burke\n')

# Close the file
    outfile.close()

# Call the main function
main()