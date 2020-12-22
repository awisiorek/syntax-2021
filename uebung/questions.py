from ipywidgets import widgets
from IPython.display import display
from ipywidgets import HBox, Label, Dropdown, Button, Checkbox, HTML, Layout
from nltk.tree import ParentedTree


single = "Wählen Sie die <ins>eine</ins> korrekte Antwort aus: "
multiple = "Markieren Sie <ins>alle</ins> passenden Antworten: "
offen = "Geben Sie die korrekte Antwort ein: "
selection = single
luecke = "Vervollständigen Sie den Lückentext: "
baum = "Erstellen Sie die den korrekten Baum durch das Füllen der Lücken: "
syntaxbaum = "Erstellen Sie die den korrekten Syntaxbaum durch das Füllen der Lücken: "
klammerausdruck = "Fügen Sie die fehlenden Klammern ein. Der entsprechende Syntaxbaum ist als Hilfestellung im zugehörigen PDF zu finden."


def aufgabe(aufg):
    for a in aufg:
        #  print(" ")
         [display(x) for x in a]


class PictureChoice(widgets.VBox):
    def __init__(self, text, correct, *wrong, inst=single):
        choices = list(wrong)
        choices.append(correct)
        choices.sort()
        pic_num = []
        for i, pic in enumerate(choices, 1):
            pic_num.append((pic, i))
                        
        def on_button_clicked(b):
            choice = b.description
            b.style.button_color = 'lightgreen' if choice == self.correct else 'red'

            if self.answered:
                return
            self.answered = True

            # textbox.layout.border = "2px solid lightgreen" if choice == self.correct else "2px solid red"

        textbox = widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(text), layout=widgets.Layout(justify_content="center"))
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst), layout=widgets.Layout(justify_content="center")) 
        imagebox = []
        for (p, n) in pic_num:
            file = open(p, "rb")
            image = file.read()
            pic = widgets.Image(value=image, format='png', width=300, height=200)
            if p == correct:
                 self.correct = str(n)

            but = widgets.Button(description=str(n), layout=widgets.Layout(width="250px"))
            but.on_click(on_button_clicked)

            picbox = widgets.VBox(children=[pic, but])
            imagebox.append(picbox)

        allpng = []
        while not imagebox == []:
             if len(imagebox) > 2:
                 allpng.append(widgets.HBox(children=[imagebox[0], imagebox[1]]))
                 imagebox.pop(0)
                 imagebox.pop(0)
             else:
                 allpng.append(widgets.HBox(children=imagebox))
                 break

        super().__init__(children=[textbox, instbox]+allpng)
        self.answered = False

class Anleitung(widgets.VBox):
    def __init__(self, text):
        textbox = widgets.HTML(value='{}'.format(text), layout=widgets.Layout(justify_content="center")) 
        super().__init__(children=[textbox])

class SingleChoice(widgets.VBox):
    def __init__(self, text, correctChoice, *wrongChoices, sonst=False, inst=single):
        choices = list(wrongChoices)
        choices.append(correctChoice)
        choices.sort()
        buttons = [widgets.Button(description=choice, layout=widgets.Layout(width="250px")) for choice in choices]
        if sonst:
            buttons.append(
                widgets.Button(
                    description="Keine der anderen Möglichkeiten",
                    layout=widgets.Layout(width="250px")
                )
            )
                
        def on_button_clicked(b):
            choice = b.description
            if b.style.button_color == 'lightgreen' or b.style.button_color == 'red':
                b.style.button_color = None
            else:    
                b.style.button_color = 'lightgreen' if choice == self.correct else 'red'
            
            
            if self.answered:
                #b.style.button_color = None
                #self.answered = False
                return
            self.answered = True

            # textbox.layout.border = "2px solid lightgreen" if choice == self.correct else "2px solid red"


        for button in buttons:
            button.on_click(on_button_clicked)
        
        allbox = []
        while not buttons == []:
            if len(buttons) > 2:
                allbox.append(widgets.HBox(children=[buttons[0], buttons[1]]))
                buttons.pop(0)
                buttons.pop(0)
            else:
                allbox.append(widgets.HBox(children=buttons))
                break

        textbox = widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(text), layout=widgets.Layout(justify_content="center"))
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst), layout=widgets.Layout(justify_content="center")) 
        super().__init__(children=[textbox, instbox]+allbox)
        self.correct = correctChoice
        self.answered = False

        
            

class OpenQuestion(widgets.VBox):
    def __init__(self, text, solution, *other_correct_choices, is_correct_fun=None, inst=None):
        self.correct_choices = list(other_correct_choices)
        self.correct_choices.append(solution)
        self.is_correct_fun = is_correct_fun

        textbox = widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(text))
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst)) 
        answer_input = widgets.Text()
        submit_button = widgets.Button(description="OK")
        give_up_button = widgets.Button(description="Lösung zeigen")
        button_box = widgets.HBox(children=[submit_button, give_up_button])

        super().__init__(children=[textbox,instbox, answer_input, button_box])
        self.answered = False

        def on_ok_button_clicked(b):
            if self.answered:
                return

            given_answer = answer_input.value
            answer_input.layout.border = '2px solid lightgreen' if self.is_correct(given_answer) else '2px solid red'

        submit_button.on_click(on_ok_button_clicked)

        def on_show_solution_button_clicked(b):
            answer_input.value = solution
            answer_input.layout.border = '2px solid lightgreen'
            answer_input.disabled = True

        give_up_button.on_click(on_show_solution_button_clicked)

    def is_correct(self, answer):
        if answer in self.correct_choices:
            return True
        if self.is_correct_fun is not None:
            return self.is_correct_fun(answer)
        return False
    
    
class SelectionList(widgets.VBox):
      
    def __init__(self, text, correct, *wrong, sonst=False, inst=selection):
        self.selection = ""
           
        self.richtig = correct    
        
        def makeAnswers(correct, wrong):    
            allAnsw = ["Keine der Alternativen"] if sonst else []
            allAnsw.extend(wrong)
            allAnsw.append(correct)
            allAnsw.sort()
            return allAnsw
        
        allAnsw = makeAnswers(correct, list(wrong))
        self.selection=allAnsw[0]
        
        textbox = widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(text))
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst), layout=widgets.Layout(justify_content="center")) 
        
        answer = widgets.Dropdown(options = allAnsw, value= allAnsw[0], description="Antwort:", layout={'width': '500px'})
        button = widgets.Button(description="Korrekt?",layout=widgets.Layout(width="250px"))
        super().__init__(children=[textbox, instbox, answer, button])
        
        def on_change_drop(change):
            if change['type'] == 'change' and change['name']=='value':
                    self.selection = change['new']
                    
            button.style.button_color = None        
                    
        answer.observe(on_change_drop)
        
        def on_button_clicked(b):
                if  self.selection == self.richtig:
                    b.style.button_color = 'lightgreen'
                else:
                    b.style.button_color = 'red'
        
        button.on_click(on_button_clicked)
    
class Lueckentext(widgets.VBox):
    def __init__(self, text, to_replace, tree=False, inst=luecke):
        # to_replace ist dictionary mit 'word':'alternative list'
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst), layout=widgets.Layout(justify_content="center")) 

        repl = to_replace
        textlist = text.split(" ")
        self.richtig = text
        zusammen =  []
        self.selection = []
        self.wid_list = []
        
        def on_change_drop(change):
            if change['type'] == 'change' and change['name']=='value':
                    index = self.wid_list.index(change.owner)
                    self.selection[index] = change['new']
            button.style.button_color = None        
        
        for word in textlist:
            try: 
                choice = repl[word]
                if not word in choice:
                    choice.append(word)
                choice.sort()
                choice.append(" ")
                zw = ' '.join(zusammen)
                self.wid_list.append(widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(zw), width='auto'))
                self.selection.append(zw)                     
                zusammen = []
                dropdown =widgets.Dropdown(options = choice, value=choice[len(choice)-1], layout=widgets.Layout(width="150px"))  
                self.wid_list.append(dropdown)
                dropdown.observe(on_change_drop)
                self.selection.append(" ")
                
            except KeyError:
                zusammen.append(word)
        
        zw = ' '.join(zusammen)
        self.wid_list.append(widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(zw)))
        self.selection.append(zw)  
        
        box_layout = widgets.Layout(display='inline-flex', flex_flow='row wrap', align_items='stretch',flex='flex-grow', justify_content='flex-start', align_content="stretch")
        box = widgets.Box(children=self.wid_list, layout=box_layout)
        
        button = widgets.Button(description="Korrekt?",layout=widgets.Layout(width="250px"))
        
        
        super().__init__(children=[instbox,box,button])
        
                
        def on_button_clicked(b):
                sel = ' '.join(self.selection)
                if  sel == self.richtig:
                    b.style.button_color = 'lightgreen'
                    # if tree:
                    #     out=""
                    #     for elem in self.richtig:
                    #         out = out + elem
                        
                    #     t = ParentedTree.fromstring(out)
                    #     display(t)
                else:
                    b.style.button_color = 'red'
        
        button.on_click(on_button_clicked)
        

class MultipleChoice(widgets.VBox):        
    def __init__(self, text, correct, wrong, sonst=False, inst=multiple):
        self.chosenList = []
        if sonst == True:
            allAnsw = ["Keine der Alternativen"] + correct + wrong
        else:
            allAnsw = correct + wrong
        allAnsw.sort()
        self.myCor = correct
        self.myCor.sort()
    
        aufgabenstellung = HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(text))
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst), layout=widgets.Layout(justify_content="center")) 
        
        button = Button(description="Korrekt?",layout=widgets.Layout(width="250px"))
        
        def on_change_check(change):
            if change['type'] == 'change' and change['name']=='value':
                if change['new'] == True:
                    box = change['owner']
                    d = box.description
                    self.chosenList.append(d)
                else:
                    box = change['owner']
                    if box.description in self.chosenList:
                        self.chosenList.remove(box.description)
            button.style.button_color = None          
            
        cb = []
        style = {'description_width': 'initial'}
        for answer in allAnsw:
            cb.append(Checkbox(value=False, description=answer, disabled=False, style=style, layout=Layout(width="600px")))
            cb[-1].observe(on_change_check)
        
        box = widgets.VBox(children=cb)
        
        super().__init__(children=[aufgabenstellung, instbox, box, button])
        
        def on_button_clicked(button):
            self.chosenList.sort()
            if self.chosenList == self.myCor:
                button.style.button_color = 'lightgreen'
            else:
                button.style.button_color = 'red'
        
        button.on_click(on_button_clicked)


class OpenTextfield(widgets.VBox):
    def __init__(self, text, initial, correct, inst=None, klammer=False):
        
        textfield = widgets.Textarea(value=initial, placeholder='Type something', description='', disabled=False, layout=Layout(width='500px'))
        # textfield.observe(on)
        textbox = widgets.HTML(value='<h4 style="font-size:14px;">{}</h4>'.format(text))
        instbox = widgets.HTML(value='<i>{}</i>'.format(inst)) 
        
        submit_button = widgets.Button(description="Korrekt?", layout=widgets.Layout(width="350px"))
        give_up_button = widgets.Button(description="Lösung zeigen", layout=widgets.Layout(width="150px"))
        button_box = widgets.HBox(children=[submit_button, give_up_button])

        super().__init__(children=[textbox, instbox, textfield, button_box])


        def on_ok_button_clicked(button):
            given_answer = textfield.value
            ans = given_answer.split()
            answer = ''.join(ans)
            corr = correct.split()
            newc = ''.join(corr)

            if answer == newc:
                button.style.button_color = 'lightgreen'
                button.description = "Richtig!"

            else:
                button.style.button_color = 'red'
                
                if klammer:
                    more = True
                    stack = []
                    not_open = 0
                    for i,c in enumerate(given_answer):
                        if c == '[':
                            stack.append(i)
                        elif c == ']' and stack:
                            stack.pop()
                        elif c == ']':
                            not_open += 1
                        elif c in ['(',')','{','}']:
                            button.description="Falsche Klammern!"
                            more = False
                            break
                    
                    if stack and more:
                        more = False
                        button.description =str(len(stack))+" Klammern schließen!"

                    if not_open and more:
                        more = False
                        button.description = str(not_open)+" Klammern öffnen!"

                    if more:
                        button.description = "Noch eine Übereinstimmung mit Synatxbaum erreicht!"

        def on_show_solution_button_clicked(button):
            textfield.value = correct
            textfield.disabled = True
            submit_button.disabled = True
            give_up_button.disabled = True

        submit_button.on_click(on_ok_button_clicked)
        give_up_button.on_click(on_show_solution_button_clicked)