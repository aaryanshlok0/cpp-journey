#include <bits/stdc++.h>

using namespace std;

int main() {

   

    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        
    
    int n,n1,k;
    int sum=0;
    cin>>n>>k;
    n1=n;
    vector <int> arr(n);
    vector <int> arr1(n1);

        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        for(int i=0;i<n1;i++){
            cin>>arr1[i];
        }

        sort(arr.begin(),arr.end());
        sort(arr1.begin(),arr1.end());
    
        int first=0;
        int last=n-1;
        for(int i=1;i<=k;i++){
        if(arr[first]<arr1[last]){
            swap(arr[first],arr1[last]);
            first++;
            last--;
        }
        else{break;}
}
   

    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    cout<<sum<<endl;

    
    }

    return 0;
}
