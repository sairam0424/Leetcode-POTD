class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def dfs(sub_expression):

            operator = sub_expression[0]

            # print(operator)

            values = sub_expression[2:-1]

            # print(values)

            if operator == '!':#if the operator is not 

                return "f" if values == "t" else "t"

            if operator == "|":#if the operator is or

                return "t" if "t" in values else "f"

            if operator == "&":#if the operator is and 

                return "f" if "f" in values else "t"

            # return "f"
            


        while len(expression)>1:

            # print(expression)

            start_index = max(expression.rfind("!") , expression.rfind("&") ,expression.rfind("|"))#rfind()-> returns the highest_index of the last occurance of the substring from the input _string

            end_index =  expression.find(")",start_index)

            # print([start_index , end_index])

            sub_expression = expression[start_index:end_index+1]

            # print(sub_expression)

            res = dfs(sub_expression)

            # print(res)

            expression = expression[:start_index] + res + expression[end_index+1:]


        return expression == "t"

        
        