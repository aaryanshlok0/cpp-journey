#include <bits/stdc++.h>

using namespace std;

int main() {


    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        int x;
        cin>>x;
        int countDiv=0;
        for(int i=1;i*i<=x;i++){
            if(x%i==0){
                countDiv+=2;
                
            }
            if(i*i==x){
                countDiv-=1;
            }
        }
        cout<<countDiv<<endl;
    }

    return 0;
}
