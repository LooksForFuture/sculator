class dynamic:
    def __init__(self,val):
        self.val = val
        self._val = None
    def eval(self):
        return eval(self.val)

    #normal operations
    def __add__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()+other
    def __sub__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()-other
    def __mul__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()*other
    def __matmul__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()@other
    def __truediv__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()/other
    def __floordiv__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()//other
    def __mod__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()%other
    def __pow__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()**other

    #bitwise operations
    def __lshift__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()<<other
    def __rshift__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()>>other
    def __and__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()&other
    def __xor__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()^other
    def __or__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval()|other

    #r normal operations
    def __radd__(self,other):
        return other+self.eval()
    def __rsub__(self,other):
        return other-self.eval()
    def __rmul__(self,other):
        return other*self.eval()
    def __rmatmul__(self,other):
        return other@self.eval()
    def __rtruediv__(self,other):
        return other/self.eval()
    def __rfloordiv__(self,other):
        return other//self.eval()
    def __rmod__(self,other):
        return other%self.eval()
    def __rpow__(self,other):
        return other**self.eval()

    #r bitwise operations
    def __rlshift__(self,other):
        return other<<self.eval()
    def __rrshift__(self,other):
        return other>>self.eval()
    def __rand__(self,other):
        return other&self.eval()
    def __rxor__(self,other):
        return other^self.eval()
    def __ror__(self,other):
        return other|self.eval()

    def __len__(self):
        return len(self.eval())
    def __getitem__(self,key):
        return self.eval()[key]
    def __iter__(self):
        self._val = self.eval()
        return iter(self._val)
    def __next__(self):
        return self._val.__next__()

    def __eq__(self, other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.eval() == other

    def __call__(self):
        return self.eval()
    def __str__(self):
        return str(self.eval())

class dynam:
    def __init__(self,val):
        self.val = val
    def eval(self):
        return eval(self.val)

    #normal operations
    def __add__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()+other
    def __sub__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()-other
    def __mul__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()*other
    def __matmul__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()@other
    def __truediv__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()/other
    def __floordiv__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()//other
    def __mod__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()%other
    def __pow__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()**other

    #bitwise operations
    def __lshift__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()<<other
    def __rshift__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()>>other
    def __and__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()&other
    def __xor__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()^other
    def __or__(self,other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val()|other

    #r normal operations
    def __radd__(self,other):
        return other+self.val()
    def __rsub__(self,other):
        return other-self.val()
    def __rmul__(self,other):
        return other*self.val()
    def __rmatmul__(self,other):
        return other@self.val()
    def __rtruediv__(self,other):
        return other/self.val()
    def __rfloordiv__(self,other):
        return other//self.val()
    def __rmod__(self,other):
        return other%self.val()
    def __rpow__(self,other):
        return other**self.val()

    #r bitwise operations
    def __rlshift__(self,other):
        return other<<self.val()
    def __rrshift__(self,other):
        return other>>self.val()
    def __rand__(self,other):
        return other&self.val()
    def __rxor__(self,other):
        return other^self.val()
    def __ror__(self,other):
        return other|self.val()

    def __len__(self):
        return len(self.val())
    def __getitem__(self,key):
        return self.val()[key]
    def __iter__(self):
        self._val = self.val()
        return iter(self._val)
    def __next__(self):
        return self._val.__next__()

    def __eq__(self, other):
        if isinstance(other, dynamic):
            other = other.eval()
        return self.val() == other

    def __call__(self):
        return self.val()
    def __str__(self):
        return str(self.val())
