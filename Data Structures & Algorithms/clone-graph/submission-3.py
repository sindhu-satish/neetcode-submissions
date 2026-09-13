# BETTER THAN NEETCODE

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def dfs(node):
            # if node not visited already
            if node in visited:
                return visited[node]

            # create copy of the node
            node_copy = Node(node.val)

            # Mark it visited before recursing
            visited[node] = node_copy

            # run dfs for all of node's neightbors
            for neighbor in node.neighbors:
                node_copy.neighbors.append(dfs(neighbor))

            return node_copy

        return dfs(node) if node else None

        