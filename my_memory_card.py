#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QHBoxLayout,QButtonGroup
from random import shuffle

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

questions_list=[]
questions_list.append(Question('6*6?','36','1','4000 000 625','...'))
questions_list.append(Question('Сколько хромосом у человека?','46','47','9','45',))
questions_list.append(Question('джоджо референс','кнш','нет','👀','да'))


app=QApplication([])
window=QWidget()
window.setWindowTitle('Memo Card')
button=QPushButton('Ответить')
lb_Question=QLabel('В каком году основалось казахское ханство?')

RadioGroupBox=QGroupBox('Варианты ответов')
otvet_1=QRadioButton('1460')
otvet_2=QRadioButton('1560')
otvet_3=QRadioButton('1449')
otvet_4=QRadioButton('1450')

RadioGroup=QButtonGroup()
layout_ans1=QVBoxLayout()
layout_ans2=QHBoxLayout()
layout_ans3=QHBoxLayout()
layout_ans2.addWidget(otvet_1)
layout_ans2.addWidget(otvet_2)
layout_ans3.addWidget(otvet_3)
layout_ans3.addWidget(otvet_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox=QGroupBox('Результат теста')
lb_Result=QLabel('прав ты или нет?')
lb_Correct=QLabel('ответ будет тут!')

layout_res=QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct,stretch=2)
AnsGroupBox.setLayout(layout_res)

ResultGroupBox=QGroupBox('Результат тестирования')
lb_Result_test=QLabel('')
layout_res_test=QVBoxLayout()
layout_res_test.addWidget(lb_Result_test, alignment=Qt.AlignCenter)
ResultGroupBox.setLayout(layout_res_test)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(ResultGroupBox)

AnsGroupBox.hide()
ResultGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)

layout_card=QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

answers=[otvet_1,otvet_2,otvet_3,otvet_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        window.points+=1
        window.questions+=1
        show_correct('Правильно!')
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            window.questions+=1

def next_question():
        window.cur_question += 1
        if window.cur_question>=len(questions_list):
            button.setText('Завершить тест')
            lb_Question.setText('Тест завершен')
        else:   
            q=questions_list[window.cur_question]
            ask(q)

def result_test():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    ResultGroupBox.show()
    lb_Result_test.setText('Вы набрали:'+str(window.points)+'из'+str(window.questions))

def click_OK():
    if button.text()=='Ответить':
        check_answer()
    elif button.text()=='Завершить тест':
        result_test()
    else:
        next_question()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    otvet_1.setChecked(False)
    otvet_2.setChecked(False)
    otvet_3.setChecked(False)
    otvet_4.setChecked(False)
    RadioGroup.setExclusive(True)

window.points=0
window.questions=0

window.cur_question=-1
button.clicked.connect(click_OK)
next_question()
window.setLayout(layout_card)
window.show()
app.exec_()    