class Solution(object):
    def simplifyPath(self, path):
        stack = []
        components = path.split('/')
        
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        # Construct simplified path
        simplified_path = '/' + '/'.join(stack)
        
        return simplified_path if simplified_path else '/'
