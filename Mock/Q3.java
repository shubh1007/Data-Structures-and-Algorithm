abstract class Hackerearth
{
    int k = 1;
    public Hackerearth(){
        show();
        k = 3;
    }
    abstract void myMethod();
    void show(){
        System.out.println(k);
    }
}

interface Hacker{
    abstract void myMethod();
}
class Hackster extends Hackerearth implements Hacker{
    public Hackster(){
        super();
        k = 2;
    }
    @Override
    public void myMethod(){
        new Hackster();
    }
}

class Hacks extends Hackster{
    public Hacks(){
        k = -1;
        myMethod();
    }
}

class Main{
    public static void main(String[] args){
        Hacks obj = new Hacks();
    }
}










