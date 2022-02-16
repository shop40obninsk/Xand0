import XandZero_Core
import tele_keyboards
import Sender_message_telegram
import random
import numpy as np

def generate_keyboard(Core, User_figure):
    out=[]
    space=[3,3,3]
    mass=Core.get()
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if mass[i][j]==2:
                if str(User_figure)=="1":
                    out.append(["X",f"M{i} {j}"])
                else:
                    out.append(["O", f"M{i} {j}"])
            else:
                out.append([" ",f"N"])
    print(mass)
    return tele_keyboards.Inline_Keyboard_Generator(out,space)


def inline_buttons_worker(bot,call,text,Core,User_figure):
    print(text)
    if "C" in text:
        text=text.replace("C","")
        User_figure=int(text)
        Core=XandZero_Core.Engine(User_figure)
        if random.randint(0, 1) == 0:
            Sender_message_telegram.replace_message(bot,None,"Первой ходит машина",call=call,keyboard=None)
            Core.Mashine_step()
            keyboard=generate_keyboard(Core, User_figure)
            Sender_message_telegram.send_message(bot, None, Core.show_place(), call=call, keyboard=keyboard)
        else:
            keyboard = generate_keyboard(Core, User_figure)
            Sender_message_telegram.replace_message(bot, None, "Первым ходит игрок", call=call, keyboard=None)
            Sender_message_telegram.send_message(bot, None, Core.show_place(), call=call, keyboard=keyboard)
        return Core,User_figure

    if "M" in text:
        text = text.replace("M", "")
        text=text.split(' ')
        X=int(text[0])
        Y=int(text[1])
        Core.User_step(X,Y)
        W=Core.Check_win()
        if W!=2:
            if W != 2:
                if int(W)==1:
                    W="X"
                else:
                    W="O"
            Sender_message_telegram.replace_message(bot, None, Core.show_place(), call=call, keyboard=None)
            Sender_message_telegram.send_message(bot, None, f"Winner is: {W}", call=call, keyboard=None)
            return Core, User_figure
        if np.array(Core.get()).reshape(-1).tolist().count(2) == 0:
            Sender_message_telegram.replace_message(bot, None, Core.show_place(), call=call, keyboard=None)
            Sender_message_telegram.send_message(bot, None, "draw", call=call, keyboard=None)
            return Core, User_figure
        else:
            Core.Mashine_step()
            W = Core.Check_win()
            if W != 2:
                if int(W)==1:
                    W="X"
                else:
                    W="O"
                Sender_message_telegram.replace_message(bot, None, Core.show_place(), call=call, keyboard=None)
                Sender_message_telegram.send_message(bot, None, f"Winner is: {W}", call=call, keyboard=None)
                return Core, User_figure
            if np.array(Core.get()).reshape(-1).tolist().count(2) == 0:
                Sender_message_telegram.replace_message(bot, None, Core.show_place(), call=call, keyboard=None)
                Sender_message_telegram.send_message(bot, None, "draw", call=call, keyboard=None)
                return Core, User_figure
        keyboard = generate_keyboard(Core, User_figure)
        Sender_message_telegram.replace_message(bot, None, Core.show_place(), call=call, keyboard=keyboard)
        return Core, User_figure