#제2행에 대한 여인수 행렬식 구하기

n = int(input("행렬의 크기 입력 : "))
if n != 3:
    print("이 프로그램은 3x3 행렬만 계산합니다.")
    exit()

A=[]
print("\n행렬의 값을 입력하세요.")
for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"{i+1} x {j+1} 행렬의 값을 입력하세요 : "))
        row.append(val)
    A.append(row)

print("입력한 행렬 A")
for row in A:
    print("     ", end = "")
    for v in row:
        print(f"{v} ", end = "")
    print()

def det2(a, b, c, d):
    return a * d - b * c

a = A[1][0] * det2(A[0][1],A[0][2],A[2][1],A[2][2])
b = A[1][1] * det2(A[0][0],A[0][2],A[2][0],A[2][2])
c = A[1][2] * det2(A[0][0],A[0][1],A[2][0],A[2][1])

det = - a + b - c

print("\n입력한 행렬의 행렬식 값")
print(f"Det(A) = {det}")