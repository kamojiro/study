#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            ret.add(local_name+"@"+domain_name)
        return len(ret)

# @lc code=end

