#include <bits/stdc++.h>

using namespace std;

int main() {

    typedef long long ll;
    ll n;
    ll moves_sum=0;

    cin>>n;
    vector<ll> arr(n);
    for(ll i=0;i<n;i++){
        cin>>arr[i];
        if(i>0){
        ll diff=arr[i]-arr[i-1];
        if(diff<0){
            
            arr[i]=arr[i-1];
            moves_sum+=abs(diff);
        
        } 
        }

        
        }
    
        cout<<moves_sum;


    return 0;
}
