# https://leetcode.com/discuss/general-discussion/638847/tree-builder-for-debugging-locally


def build_tree(s):
    s = s[1:-1].split(',')
    if len(s) == 0:
        return
    nodes = [('root', s[0])]
    for i, c in enumerate(s[1:]):
        if c != 'null':
            if i & 1:
                nodes.append((nodes[i // 2][0] + '.right', c))
            else:
                nodes.append((nodes[i // 2][0] + '.left', c))
    for node in nodes:
        print(node[0] + ' = TreeNode(' + node[1] + ')')

# build_tree('[1,0,0,0,0,0,1,null,null,null,1,0,null,null,0]')
