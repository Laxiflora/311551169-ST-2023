/*
Enter month1: 
Enter day1: 
Enter month2: 
Enter day2: 
Enter year: 
Result is: 0

*/
import org.junit.Assert;
import org.junit.Test;

public class CalTest{
    //Normal year
    @Test
    public void test1(){
        Assert.assertEquals(151, Cal.cal(5, 23, 10, 21, 2022));
    }
    // leap year
    @Test
    public void test2(){
        Assert.assertEquals(121, Cal.cal(1, 1, 5, 1, 2020));
    }
    // (m100==0) && (m400!=0)
    @Test
    public void test3(){
        Assert.assertEquals(181, Cal.cal(1, 1, 7, 1, 2100));
    }

    //(m100==0) && (m400==0)
    @Test
    public void test4(){
        Assert.assertEquals(182, Cal.cal(1, 1, 7, 1, 2000));
    }

    // same month
    @Test
    public void test5(){
        Assert.assertEquals(14, Cal.cal(1, 7, 1, 21, 2100));
    }
    //Normal year with month 1
    @Test
    public void test6(){
        Assert.assertEquals(59, Cal.cal(1, 1, 3, 1, 2022));
    }

    // test day2 < day1
    @Test
    public void test7(){
        Assert.assertEquals(-6, Cal.cal(8, 7, 8, 1, 2022));
    }

    //same day
    @Test
    public void test8(){
        Assert.assertEquals(0, Cal.cal(7, 7, 7, 7, 2022));
    }

}