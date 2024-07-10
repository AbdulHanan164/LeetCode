class Solution(object):
    def minOperations(self, logs):
        stack = []
        
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if stack:
                    stack.pop()
            else:
                # it's a directory change
                # Remove the trailing slash and push the directory to stack
                directory = log[:-1]
                stack.append(directory)
        
        return len(stack)
