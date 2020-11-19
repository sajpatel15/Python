''' Module lab07.py '''
from socket import *
import threading, random

class HighCardServer:
    
    # method to initialize the class
    def __init__(self, addr, port, backlog):
        self.addr = addr
        self.port = port
        self.backlog = backlog




    # method that runs a loop to accept connections     
    def accept_connections(self):
        while True:
            c, a = self.s.accept()
            t = threading.Thread(target=self.deal_with_client, args =(c, a), daemon=True)
            t.start()        

    # method that handles client connections
    def deal_with_client(self, client, addr):
        string = "Connected to "
        string += str(client)
        string += ".\n"
        client.send(string.encode())
        
        # sending a welcome message
        welcome = "Hello, welcome to The High Card Server!\n"
        client.send(welcome.encode())
        
        # creating a dictionary with the cards
        cards = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "J", 12: "Q", 13: "K", 14: "A"}
        
        # creating random numbers between 2 and 14 for the player and the dealer
        dealer_num = random.randint(2,14)
        player_num = random.randint(2,14)
        
        # getting the card for the players
        dealer_card = cards[dealer_num]
        player_card = cards[player_num]
        
        # sending the client info for the dealt cards
        dealer = "The dealer has " + str(dealer_card) + "\n"
        player = "You have "+ str(player_card) + "\n"
        
        client.send(dealer.encode())
        client.send(player.encode())
        
        # deciding who wins and sending the client the results
        if player_num > dealer_num:
            win = "You win!\n"
            client.send(win.encode())
        elif player_num == dealer_num:
            tie = "It's a tie!\n"
            client.send(tie.encode())   
        else:
            lose = "Dealer wins!\n"
            client.send(lose.encode())
        
        # sending goodbye message
        goodbye = "Goodbye...Connection closed by foreign host.\n"
        client.send(goodbye.encode())
         
        # closing the client connection
        client.close()
        
        
        
            
    # method that starts the server     
    def start_server(self):
        # binding the socket to the given address and port
        self.s = socket()
        self.s.bind((self.addr, self.port))
        
        # starting to listen on the socket
        self.s.listen(5)
        
        # starting a non-blocking infinite loop
        t1 = threading.Thread(target = self.accept_connections)
        t1.start()
       

        
