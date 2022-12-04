#Top 10 AWS security tools

# empty list
security_tools = []

#Populate the list using append or insert
security_tools.append('AWS Identity and Access Management (IAM)')
security_tools.append('Amazon GuardDuty')
security_tools.append('Amazon Macie')
security_tools.append('AWS Config')
security_tools.append('AWS CloudTrail')
security_tools.append('Security Hub')

# Application Security tools
security_tools.append('AWS Shield')
security_tools.append('AWS Web Application Firewall')
security_tools.append('AWS Secrets Manager')

# To remove items from this list
security_tools.remove('Security Hub')
security_tools.remove('Amazon GuardDuty')
security_tools.remove('Amazon Macie')

# To print items from my list
print(security_tools)
print(len(security_tools))
