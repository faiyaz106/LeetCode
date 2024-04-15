class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate=list(senate)
        R=[]
        D=[]
        for i,v in enumerate(senate):
            if v=="R":
                R.append(i)
            if v=="D":
                D.append(i)
        while R and D: 
            R_idx=R.pop(0)
            D_idx=D.pop(0)
            if R_idx<D_idx:
                R.append(R_idx+len(senate))
            else:
                D.append(D_idx+len(senate))
        return "Dire" if D else "Radiant"
            