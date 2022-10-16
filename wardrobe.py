class Wardrobe:
    default=['prada','Dior','Givenchy',
    'fendi',   'versace', 'gucci']
    d_basket=[]
    c_basket=[]
    def __init__(self,gender,default=default,d_basket=d_basket,c_basket=c_basket):
        self.default =default
        self.c_basket=c_basket
        self.d_basket=d_basket
    def __str__(self):
        return 'wardrobe info: \n wardrobe: {}\n clean_basket:{}\n dirty_basket: {}\n'.format(self.default,self.c_basket,self.d_basket)
        
    def wear(self,choice):
        if choice in self.default:
            print(choice,'worn successfully')
            self.default.pop(self.default.index(choice))
            self.d_basket.append(choice)
        else: print('oops!',choice,'is not in your wardrobe collection')
        
        
    def buy(self,brand=None):
        self.brand=brand
        self.brand=input('which brand would you like to add to your collection ')
        count=self.default.count(self.brand) +self.d_basket.count(self.brand) +self.c_basket.count(self.brand)
        print('count is',count)
        while self.brand:
            print(self.default,'this')
            if (self.brand in self.default) or (self.brand in self.d_basket) or (self.brand in self.c_basket):
                confirm=input('{} already in your collection,type "yes" to continue or "no" to abort '.format(self.brand))
                if confirm=='yes':
                    self.default.append(self.brand +str(count+1))
                    break
                elif confirm=='no':break
                
            else: self.default.append(self.brand);break
            
    def wash(self,brand):
            self.brand=brand
            if brand in self.d_basket:
                self.c_basket.append(brand)
                print('washed successfully')
                self.d_basket.pop(self.d_basket.index(brand))
            elif brand in self.default or brand in self.c_basket: print('oops,we cant waste detergent on a clean clothe')
            else:print('comrade,you cant wash what you don have')
            
            
            
    def hang(self,brand):
        self.brand=brand
        if brand in self.c_basket:
            self.default.append(brand)
            self.c_basket.pop(self.c_basket.index(brand))
            
        else:print('something is not right')
        
        
    def burn(self,*args):
        self.args=args
        for i in self.args:
            if i in self.default : self.default.pop(self.default.index(i)); print(i,'burnt')
            elif i in self.c_basket :self.c_basket.pop(self.c_basket.index(i)); print(i,'burnt')
            elif i in self.d_basket: self.d_basket.pop(self.d_basket.index(i)); print(i,'burnt')
            
            else:print('burn unsuccessful')
        
if __name__ == "__main__" :
    seun=Wardrobe('Male')
    print(seun)
    seun.wear('gucci')
    print(seun)
    #seun.buy()
    seun.wash('gucci')
    print(seun)
    seun.hang('gucci')
    seun.burn('gucci','pencil','biro','fendi','Dior')
    print(seun)
        