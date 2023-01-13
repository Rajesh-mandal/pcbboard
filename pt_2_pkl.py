import torch
import pickle 

#load the pytorch mode
# model = torch.load('C:/Users/Rajesh.Mandal/OneDrive - Neudesic/Download/initiative/Flask/pcb_board_detection/PCB_Board_Flask/best_100epoch.pt',map_location='cpu')

# #load into pickle file 

# with open('pcb_board.pkl','wb') as fl:
#     pickle.dump(model, fl)

#convert pickle to .pt

with open('pcb_board.pkl','rb') as fl:
    model = pickle.load(fl)

torch.save(model, 'model.pt')
