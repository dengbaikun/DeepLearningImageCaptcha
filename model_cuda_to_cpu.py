import torch

from model import CNN

if __name__ == '__main__':
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    cnn = CNN()
    cnn.to(device)
    cnn.eval()
    cnn.load_state_dict(torch.load('best_model.pkl'))
    cnn = cnn.cpu()
    torch.save(cnn.state_dict(), "./cpu-model.pkl")
    print("save model")