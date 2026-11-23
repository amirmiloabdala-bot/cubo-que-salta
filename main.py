import pygame
import random
pygame.init()
pygame.mixer.init()
#sonidos
sonido_salto = pygame.mixer.Sound("salto.mp3")
sonido_salto.set_volume(1.0)
sonido_muerte = pygame.mixer.Sound("muerte.mp3")
sonido_muerte.set_volume(1.0)
sonido_click = pygame.mixer.Sound("click.mp3")
sonido_explosion = pygame.mixer.Sound("explosion.mp3")
sonido_fwosh = pygame.mixer.Sound("fwosh.mp3")

pantalla = pygame.display.set_mode((600,1300))
relog = pygame.time.Clock()
vivo = False
perdio = False
jefe = False
cinematica = False
gano = False
vida_jefe = 110
#personajes y enemigos    lado altura   tamaño
cuadrado = pygame.Rect((100,1000),(100,100))
cuadrado1 = pygame.Rect((200,200),(100,100))
enemigo = pygame.Rect((1000,1020),(60,80))
boss = pygame.Rect((200,4050),(400,400))
enemigo1 = pygame.Rect((200,4500),(70,70))
enemigo2 = pygame.Rect((350,4500),(70,70))
pelota =pygame.Rect((300,1800),(80,80))
vida_jefen = pygame.Rect((590,90),(100,1020))
#piso
pasto = pygame.Rect((0,1100),(1000,50))
pasto1 = pygame.Rect((150,1800),(50,1500))
#botones
boton = pygame.Rect((200,600),(300,200))
boton1 = pygame.Rect((200,500),(300,200))
boton2 = pygame.Rect((0,500),(150,500))
boton3 = pygame.Rect((0,100),(150,300))
boton4 = pygame.Rect((0,1100),(150,300))
boton5 = pygame.Rect((100,700),(500,300))
#texto
puntos = 0
fuente = pygame.font.SysFont(None,100)
fuente1 = pygame.font.SysFont(None,60)
texto3 = fuente.render("el cubo que salta",True,(0,0,0))
texto4 = fuente.render("jugar",True,(0,0,0))
texto5 = fuente.render("GANASTE",True,(0,0,0))
texto6 = fuente.render("volver  a jugar",True,(0,0,0))
texto7 = fuente.render("gira el telefono",True,(0,0,0))

velocidad = 0
velocidad1 = 0
ataque = random.choice([1,2])
contra = 300
#cuanto aumentan por vez
velocidad_enemigo = 10
salto = 30
caida = 2
salto1 = 30
caida1 = 2
 
#cambiar musica
def cambiar_musica(nombre):
 	pygame.mixer.music.stop()
 	pygame.mixer.music.load(nombre)
 	pygame.mixer.music.play(-1)
def reiniciar():
     global puntos,salto,caida,velocidad_enemigo,enemigo,cuadrado,pasto
     puntos = 0
     salto = 30
     caida = 2
     velocidad_enemigo = 10
     enemigo.x = 1000
     cuadrado.y = 1000
     cuadrado.x = 100
     pasto.y = 1100
     pasto.x = 0
cambiar_musica("musica_lobby.mp3")
 
while True:
	# ---------------------------------------------
	if vivo == False and perdio == False and jefe == False and cinematica == False and gano == False:
		#texturas
		pantalla.fill((100,100,200))
		pantalla.blit(texto3,(70,250))
		pygame.draw.rect(pantalla,(255,255,0),boton1)
		pantalla.blit(texto4,(boton1.x + 70,boton1.y + 60))
		#clicks
		for ev in pygame.event.get():
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if boton1.collidepoint(ev.pos):
					vivo = True
					sonido_click.play()
					cambiar_musica("musica_partida.mp3")
		
		relog.tick(30)
		pygame.display.flip()
# ---------------------------------------------
	if vivo == True:
		if puntos > 9:
			vivo = False
			cinematica = True
			cambiar_musica("musica_jefe.mp3")
			pasto1.y = 1800
			pelota.y = 2000
			boss.y = 2000
			enemigo1.y = 4500
			enemigo2.y = 4500
			vida_jefe = 110
			contra = 300
		if cuadrado.colliderect(enemigo):
			sonido_muerte.play()
			vivo = False
			perdio = True
			cambiar_musica("musica_lobby.mp3")
			
		#movimiento enemigo y aumento de velocidad
		enemigo.x -= velocidad_enemigo
		if enemigo.x < -80:
			enemigo.x = 1000
			velocidad_enemigo += 2.5
			salto += 7
			caida += 1.5
			puntos += 1
					
		#salto
		cuadrado.y -= velocidad
		if cuadrado.y > 1000:
			cuadrado.y = 1000
			velocidad = 0
			sonido_salto.play()
		if cuadrado.y < 1000:
			velocidad -= caida
		#click
		for ev in pygame.event.get():
			if ev.type == pygame.MOUSEBUTTONDOWN and cuadrado.y == 1000:
				velocidad = salto
		#jugador y fondo
		pantalla.fill((100,100,200))
		pygame.draw.rect(pantalla,(0,150,0),pasto)
		pygame.draw.rect(pantalla,(255,0,0),cuadrado)
		#pincho
		pygame.draw.polygon(pantalla,(0,0,200),[(enemigo.x + 40,enemigo.y),(enemigo.x,enemigo.y + 80),(enemigo.x + 80,enemigo.y + 80)])
		#contador de puntos
		texto = fuente.render("puntos "+ str(puntos),True,(0,0,0))
		pantalla.blit(texto,(100,100))
		
		relog.tick(30)
		pygame.display.flip()
	#----------------------------------------
	if perdio == True:
		#botones
		pantalla.fill((200,0,0))
		texto1 = fuente1.render("perdiste hiciste " + str(puntos) + " puntos",True,(0,0,0))
		pantalla.blit(texto1,(100,500))
		pygame.draw.rect(pantalla,(255,255,0),boton)
		texto2 = fuente1.render("volver a jugar",True,(0,0,0))
		pantalla.blit(texto2,(boton.x + 25,boton.y + 80))
		#volver a jugar
		for ev in pygame.event.get():
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if boton.collidepoint(ev.pos):
					reiniciar()
					#reiniciar todo
					perdio = False
					vivo = True
					sonido_click.play()
					cambiar_musica("musica_partida.mp3")
		
		relog.tick(30)
		pygame.display.flip()
	#-----------------------------------------
	if cinematica == True:
		if cuadrado.y > 200:
			cuadrado.y -= 10
		if cuadrado.y < 200:
			cuadrado.y = 200
		if cuadrado.x < 200:
			cuadrado.x += 10
		if cuadrado.x > 200:
			cuadrado.x = 200
		if pasto.x > -2000:
			pasto.x -= 20
		if pasto.x < -2000:
			pasto.x = -2000
		if pasto1.y > 0:
			pasto1.y -= 20
		if pasto1.y < 0:
			pasto1.y = 0
		if boss.y > 1050:
			boss.y -= 15
		if boss.y < 1050:
			boss.y = 1050
		
		if cuadrado.y == 200 and cuadrado.x == 200 and pasto.x == -2000 and pasto1.y == 0 and boss.y == 1050:
			cinematica = False
			jefe = True
		
		pantalla.fill((100,100,200))
		pygame.draw.rect(pantalla,(0,150,0),pasto)
		pygame.draw.rect(pantalla,(0,150,0),pasto1)
		pygame.draw.rect(pantalla,(255,0,0),cuadrado)
		pygame.draw.rect(pantalla,(0,0,100),boss)
		pantalla.blit(texto7,(100,300))
		
		relog.tick(30)
		pygame.display.flip()
	#--------------------------------------
	if jefe == True:
		if vida_jefe < 9:
			jefe = False
			gano = True
			cambiar_musica("musica_lobby.mp3")
		if contra == 0 and pelota.y > 1600:
			pelota.x = random.randint(200,400)
			pelota.y = random.randint(100,800)
		if contra > 0:
			contra -= 1
			if pelota.x < 350:
				pelota.x += 10
			elif pelota.y < 1000:
				pelota.y += 15
			if pelota.y > 999 and pelota.y != 1800:
				pelota.y = 1800
				vida_jefe -= 10
				puntos += 1
				sonido_explosion.play()
		if cuadrado1.colliderect(pelota) and contra == 0:
			contra += 200
			sonido_fwosh.play()
			
		cuadrado1.x += velocidad1
		
		if cuadrado1.x < 200:
			cuadrado1.x = 200
			velocidad1 = 0
			sonido_salto.play()
		if cuadrado1.x > 200:
			velocidad1 -= caida1
		if cuadrado1.y < 0:
			cuadrado1.y = 0
		if cuadrado1.y > 950:
			cuadrado1.y = 950
		if cuadrado1.colliderect(enemigo1):
			sonido_muerte.play()
			jefe = False
			perdio = True
			cambiar_musica("musica_lobby.mp3")
		if cuadrado1.colliderect(enemigo2):
			sonido_muerte.play()
			jefe = False
			perdio = True
			cambiar_musica("musica_lobby.mp3")
		if ataque == 1:
			enemigo1.y -= 20
			if enemigo1.y < - 50:
				enemigo1.y = random.randint(1500,1800)
				ataque = random.choice([1,2])
		if ataque == 2:
			enemigo2.y -= 20
			if enemigo2.y < -50:
				enemigo2.y = random.randint(1500,1800)
				ataque = random.choice([1,2])
		
			#click
		for ev in pygame.event.get():
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if boton2.collidepoint(ev.pos):
					if cuadrado1.x == 200:
						velocidad1 = salto1
		if pygame.mouse.get_pressed()[0]:
			pos = pygame.mouse.get_pos()
			if boton3.collidepoint(pos):
				cuadrado1.y -= 10
			if boton4.collidepoint(pos):
				cuadrado1.y += 10
		#fondo,jugador,botones
		pantalla.fill((100,100,200))
		pygame.draw.rect(pantalla,(255,0,0),cuadrado1)
		pygame.draw.rect(pantalla,(0,150,0),pasto1)
		pygame.draw.rect(pantalla,(255,255,0),boton2)
		pygame.draw.rect(pantalla,(255,255,0),boton3)
		pygame.draw.rect(pantalla,(255,255,0),boton4)
		pygame.draw.rect(pantalla,(0,0,100),boss)
		vida_jefev = pygame.Rect((600,100),(80,vida_jefe * 10))
		pygame.draw.rect(pantalla,(0,0,0),vida_jefen)
		pygame.draw.rect(pantalla,(0,255,0),vida_jefev)
		#ataque del jugador
		pygame.draw.circle(pantalla,(150,0,0),(pelota.x + 40,pelota.y + 40),50)
		#pinchos
		pygame.draw.polygon(pantalla,(0,0,200),[(enemigo1.x ,enemigo1.y),(enemigo1.x,enemigo1.y + 70),(enemigo1.x + 70,enemigo1.y + 35)])
		pygame.draw.polygon(pantalla,(0,0,200),[(enemigo2.x + 35,enemigo2.y),(enemigo2.x,enemigo2.y + 70),(enemigo2.x + 70,enemigo2.y + 70)])
		
		relog.tick(30)
		pygame.display.flip()
	#--------------------------------
	if gano == True:
		pantalla.fill((255,255,0))
		pantalla.blit(texto5,(200,200))
		pygame.draw.rect(pantalla,(0,255,0),boton5)
		pantalla.blit(texto6,(boton5.x,boton5.y + 120))
		for ev in pygame.event.get():
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if boton5.collidepoint(ev.pos):
					gano = False
					reiniciar()
					sonido_click.play()
					cambiar_musica("musica_lobby.mp3")
		
		relog.tick(30)
		pygame.display.flip()
