module Task7 where

import qualified Data.Matrix as M

-- Ковалев А.И.
-- ПИ19-3

-- Задача 3. Написать программу для выполнения действий
-- поворота и сдвига геометрических фигур (точка, куб, параллелепипед)

data Vec3D = Vec3D {x_ :: Double, y_ :: Double, z_ :: Double} deriving (Show)

type Point = Vec3D

data Axis = X | Y | Z | Axis Double Double Double

data Shape3D
  = Cube {center_ :: Vec3D, r_ :: Double}
  | Ball {center_ :: Vec3D, r_ :: Double}
  | Parallelepiped {p0_ :: Vec3D, p1_ :: Vec3D, p2_ :: Vec3D, p3_ :: Vec3D}
  deriving (Show)

verify :: Shape3D -> Shape3D
verify s@(Cube _ a)
  | a <= 0 = error "VerifyError (Cube _ a): must be positive"
  | otherwise = s
verify s@(Ball _ r)
  | r <= 0 = error "VerifyError (Ball _ r): must be positive"
  | otherwise = s
verify s@(Parallelepiped p0 p1 p2 p3)
  | isCollinear a b || isCollinear a c || isCollinear b c = error "VerifyError Parallelepiped: vectors don't have to be collinear"
  | otherwise = s
  where
    a = norm p0 p1
    b = norm p0 p2
    c = norm p0 p3

--------------- helpers
-----------------------

norm :: Point -> Point -> Vec3D
norm (Vec3D x0 y0 z0) (Vec3D x1 y1 z1) = Vec3D (x1 - x0) (y1 - y0) (z1 - z0)

isCollinear :: Vec3D -> Vec3D -> Bool
isCollinear (Vec3D x0 y0 z0) (Vec3D x1 y1 z1) = (y0 * z1 - z0 * y1 == 0) && (z0 * x1 - x0 * z1 == 0) && (x0 * y1 - y0 * x1 == 0)

-----------------------

-- матрица поворота: вращение вокруг осей X, Y, Z и произвольной оси
mAxis :: Axis -> Double -> M.Matrix Double
mAxis X alpha =
  M.fromLists
    [ [1, 0, 0],
      [0, cos alpha, - (sin alpha)],
      [0, sin alpha, cos alpha]
    ]
mAxis Y alpha =
  M.fromLists
    [ [cos alpha, 0, sin alpha],
      [0, 1, 0],
      [- (sin alpha), 0, cos alpha]
    ]
mAxis Z alpha =
  M.fromLists
    [ [cos alpha, - (sin alpha), 0],
      [sin alpha, cos alpha, 0],
      [0, 0, 1]
    ]
mAxis (Axis x y z) alpha =
  M.fromLists
    [ [cos' + (1 - cos') * x * x, (1 - cos') * x * y - sin' * z, (1 - cos') * x * z + sin' * y],
      [(1 - cos') * y * x + sin' * z, cos' + (1 - cos') * y * y, (1 - cos') * y * z - sin' * x],
      [(1 - cos') * z * x - sin' * y, (1 - cos') * z * y + sin' * x, cos' + (1 - cos') * z * z]
    ]
  where
    cos' = cos alpha
    sin' = sin alpha

-- вращение точки вокруг оси
rotateXYZ :: Point -> Axis -> Double -> Point
rotateXYZ (Vec3D x y z) ax alpha = Vec3D x' y' z'
  where
    x' = M.getElem 1 1 m
    y' = M.getElem 2 1 m
    z' = M.getElem 3 1 m
    m = M.multStd (mAxis ax alpha) v
    v = M.fromLists [[x], [y], [z]]

-- перемещение точки
movePoint :: Point -> Vec3D -> Point
movePoint (Vec3D x y z) (Vec3D dx dy dz) = Vec3D (x + dx) (y + dy) (z + dz)

-- поворот Shape3D
rotate :: Shape3D -> Axis -> Double -> Shape3D
rotate (Cube center a) ax angle = Cube (rotateXYZ center ax angle) a
rotate (Ball center r) ax angle = Ball (rotateXYZ center ax angle) r
rotate (Parallelepiped p0 p1 p2 p3) ax angle = Parallelepiped (rotate' p0) (rotate' p1) (rotate' p2) (rotate' p3)
  where
    rotate' p = rotateXYZ p ax angle

-- перемещение Shape3D
move :: Shape3D -> Vec3D -> Shape3D
move (Cube center a) vec = Cube (movePoint center vec) a
move (Ball center r) vec = Ball (movePoint center vec) r
move (Parallelepiped p0 p1 p2 p3) vec = Parallelepiped (move' p0) (move' p1) (move' p2) (move' p3)
  where
    move' p = movePoint p vec

main :: IO ()
main = do
  let point = Vec3D 2 3 4

  putStrLn "-- Point rotation around axis"
  print (rotateXYZ point X 30)
  print (rotateXYZ point Y 60)
  print (rotateXYZ point Z 90)
  print (rotateXYZ point (Axis 1 1 1) 45)
  print (rotateXYZ point (Axis 2 0 2) 90)

  putStrLn "\n-- Point moving"
  print (movePoint point (Vec3D 2 0 0))
  print (movePoint point (Vec3D 2 4 6))

  let cube = verify (Cube (Vec3D 1 1 1) 3)
  let ball = verify (Cube (Vec3D (-1) (-1) (-1)) 7)
  let prlpd = verify (Parallelepiped (Vec3D 0 0 0) (Vec3D 2 0 0) (Vec3D 2 2 0) (Vec3D 0 2 0))

  putStrLn "\n-- Cube rotation"
  print (rotate cube X 30)
  print (rotate cube (Axis 1 1 1) 45)

  putStrLn "\n-- Cube moving"
  print (move cube (Vec3D 3 0 0))
  print (move cube (Vec3D 3 2 1))

  putStrLn "\n-- Ball rotation"
  print (rotate ball Y 45)
  print (rotate ball (Axis 1 1 3) 90)

  putStrLn "\n-- Ball moving"
  print (move ball (Vec3D 3 0 0))
  print (move ball (Vec3D 3 2 1))

  putStrLn "\n-- Parallelepiped rotation"
  print (rotate prlpd Z 60)
  print (rotate prlpd (Axis 2 0 1) 90)

  putStrLn "\n-- Parallelepiped moving"
  print (move prlpd (Vec3D (-1) (-1) (-1)))
  print (move prlpd (Vec3D 0 0 3))

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

-- | -- Point rotation around axis
-- | Vec3D {x_ = 2.0, y_ = 4.414880846034199, z_ = -2.3470890727282496}
-- | Vec3D {x_ = -3.124068445239179, y_ = 3.0, z_ = -3.2000306794561917}
-- | Vec3D {x_ = -3.5781372230600135, y_ = 0.44377247881360526, z_ = 4.0}
-- | Vec3D {x_ = 6.17364960281001, y_ = 4.146261018025385, z_ = 7.22429358044547}
-- | Vec3D {x_ = 28.493639573238397, y_ = -4.920207502789742, z_ = 38.325452304186754}
-- |
-- | -- Point moving
-- | Vec3D {x_ = 4.0, y_ = 3.0, z_ = 4.0}
-- | Vec3D {x_ = 4.0, y_ = 7.0, z_ = 10.0}
-- |
-- | -- Cube rotation
-- | Cube {center_ = Vec3D {x_ = 1.0, y_ = 1.142283073980446, z_ = -0.8337801742052777}, r_ = 3.0}
-- | Cube {center_ = Vec3D {x_ = 1.9493560223645405, y_ = 1.9493560223645405, z_ = 1.9493560223645405}, r_ = 3.0}
-- |
-- | -- Cube moving
-- | Cube {center_ = Vec3D {x_ = 4.0, y_ = 1.0, z_ = 1.0}, r_ = 3.0}
-- | Cube {center_ = Vec3D {x_ = 4.0, y_ = 3.0, z_ = 2.0}, r_ = 3.0}
-- |
-- | -- Ball rotation
-- | Cube {center_ = Vec3D {x_ = -1.3762255133518482, y_ = -1.0, z_ = 0.3255815357163887}, r_ = 7.0}
-- | Cube {center_ = Vec3D {x_ = -5.004301137315565, y_ = -8.580287791717796, z_ = -21.27303062580838}, r_ = 7.0}
-- |
-- | -- Ball moving
-- | Cube {center_ = Vec3D {x_ = 2.0, y_ = -1.0, z_ = -1.0}, r_ = 7.0}
-- | Cube {center_ = Vec3D {x_ = 2.0, y_ = 1.0, z_ = 0.0}, r_ = 7.0}
-- |
-- | -- Parallelepiped rotation
-- | Parallelepiped {p0_ = Vec3D {x_ = 0.0, y_ = 0.0, z_ = 0.0}, p1_ = Vec3D {x_ = -1.9048259608303126, y_ = -0.6096212422044334, z_ = 0.0}, p2_ = Vec3D {x_ = -1.2952047186258793, y_ = -2.514447203034746, z_ = 0.0}, p3_ = Vec3D {x_ = 0.6096212422044334, y_ = -1.9048259608303126, z_ = 0.0}}
-- | Parallelepiped {p0_ = Vec3D {x_ = 0.0, y_ = 0.0, z_ = 0.0}, p1_ = Vec3D {x_ = 10.68844169677502, y_ = 1.7879933272011157, z_ = 5.79229446451668}, p2_ = Vec3D {x_ = 8.900448369573905, y_ = 0.8918460949427754, z_ = 9.368281118918912}, p3_ = Vec3D {x_ = -1.7879933272011157, y_ = -0.8961472322583403, z_ = 3.5759866544022314}}
-- |
-- | -- Parallelepiped moving
-- | Parallelepiped {p0_ = Vec3D {x_ = -1.0, y_ = -1.0, z_ = -1.0}, p1_ = Vec3D {x_ = 1.0, y_ = -1.0, z_ = -1.0}, p2_ = Vec3D {x_ = 1.0, y_ = 1.0, z_ = -1.0}, p3_ = Vec3D {x_ = -1.0, y_ = 1.0, z_ = -1.0}}
-- | Parallelepiped {p0_ = Vec3D {x_ = 0.0, y_ = 0.0, z_ = 3.0}, p1_ = Vec3D {x_ = 2.0, y_ = 0.0, z_ = 3.0}, p2_ = Vec3D {x_ = 2.0, y_ = 2.0, z_ = 3.0}, p3_ = Vec3D {x_ = 0.0, y_ = 2.0, z_ = 3.0}}
