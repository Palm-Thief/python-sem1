st = 'aboba'
file = '12bubdd22j456653d3j32jdj2dj2dj2'

st = list(st)
for each in file:
        if each.isdigit():
            st.append(each)
st = ''.join(st)


print(st)
