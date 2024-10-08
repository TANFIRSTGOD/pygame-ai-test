def trackTarget(enemyX, enemyY, enemySpeed, playerX, playerY):
    newenemyX = enemyX
    newenemyY = enemyY

    if playerX - enemyX > 0:
        newenemyX += 1
    elif playerX - enemyX < 0:
        newenemyX -= 1
    
    if playerY - enemyY > 0:
        newenemyY += 1
    elif playerY - enemyY < 0:
        newenemyY -= 1

    return [newenemyX, newenemyY]