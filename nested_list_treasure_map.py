row1=['⬜️', '⬜️', '⬜️']
row2=['⬜️', '⬜️', '⬜️']
row3=['⬜️', '⬜️', '⬜️']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where you want to put the treasure?:") #23- column 2 , row 3

#print(f"{row1}\n{row2}\n{row3}")
digit_split=(list(position))
#print(digit_split)

map[int(digit_split[1])-1][int(digit_split[0])-1]="X"
print(f"{row1}\n{row2}\n{row3}")