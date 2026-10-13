#include <bits/stdc++.h>

using namespace std;

int main() {
    
    typedef long long ll;
    ll n;
    cin>>n;
    ll x;
    cin>>x;
    
    ll gondolas_count=0;
    vector<ll> arr(n);
    for(ll i=0;i<n;i+=1){
        cin>>arr[i];
    }

    sort(arr.begin(), arr.end());
    
    ll left=0;
    ll right=n-1;
    while(left<=right){
        if(arr[left]+arr[right]<=x){
            gondolas_count++;
            left+=1;
            right-=1;
        }
        else{
            gondolas_count++;
            right-=1;
        }
    
    }

    cout << gondolas_count;

    return 0;
}
