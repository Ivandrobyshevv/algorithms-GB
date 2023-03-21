from Task4.main import RedBlackTree

if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(70)
    bst.insert(60)
    bst.insert(85)
    bst.insert(80)
    bst.insert(95)
    bst.insert(65)

    bst.print_tree()
    print("\nAfter deleting an element")
    bst.delete_node(80)
    bst.print_tree()