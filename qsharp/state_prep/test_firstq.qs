namespace hello_world {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    
    @EntryPoint()
    operation state_preparation(q: Qubit, nums: float[]) : Result {
    X(q)
    return q;
}
    
}
