# 파일명 정렬

def solution(files):
    answer = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        num_check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                num_check = True
            elif num_check == False:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))
    answer.sort(key=lambda x: (x[0].lower(), int(x[1]))) # 첫번째 요소 lower해서 정렬, 두번째 요소 int로 변환해서 정렬
    return [''.join(tup) for tup in answer]

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]