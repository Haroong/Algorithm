import sys

def get_generatl_mood(sad, happy):
    mood = ''

    if sad == 0 and happy == 0:
        mood = 'none'
    elif sad == happy:
        mood = 'unsure'
    elif sad > happy:
        mood = 'sad'
    else:
        mood = 'happy'
    
    return mood

# 입력값의 이모티콘 개수에 따라 분위기를 판별한다
def check_text_message_emoticon(text):
    sad, happy = 0, 0

    for i in range(len(text)):
        if text[i:i+3] == ':-(':
            sad += 1
        elif text[i:i+3] == ':-)':
            happy += 1
    
    res = get_generatl_mood(sad, happy)
    return res

# main
if __name__ == '__main__':
    text_message = sys.stdin.readline().rstrip()
    answer = check_text_message_emoticon(text_message)
    print(answer)