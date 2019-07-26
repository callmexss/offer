#include <mutex>
#include <iostream>

class SingleTon
{
public:
    static SingleTon& getInstance()
    {
        static SingleTon instance; // guaranteed to be destroyed.
                                   // Instantiated on first use.
        return instance;
    }
private:
    SingleTon() {}                 // Constructor? (the {} brackets) are needed here.

    // C++ 03
    // ========
    // Don't forget to declare these two. You want to make sure they
    // are unacceptable otherwise you may accidentally get copies of
    // your singleton appearing.
    // SingleTon(const SingleTon &);              // Don't Implement
    // void operator=(SingleTon const&);          // Don't implement

    // C++ 11
    // =======
    // We can use the better technique of deleting the methods
    // we don't want.
public:
    SingleTon(const SingleTon&) = delete;
    void operator=(const SingleTon&) = delete;
};



int main(int argc, const char *argv[])
{
    std::cout << &(SingleTon::getInstance()) << std::endl;
    std::cout << std::endl;
    std::cout << &(SingleTon::getInstance()) << std::endl;
    
    return 0;
}
