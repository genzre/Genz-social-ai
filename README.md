function getTier(address _owner) public view returns (string memory) {
    uint256 balance = balanceOf(_owner);
    if (balance >= 10) return \"Matrix Leader\";
    if (balance >= 3) return \"Matrix Disruptor\";
    return \"Matrix Breaker\";
}
