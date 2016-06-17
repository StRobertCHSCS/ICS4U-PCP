using UnityEngine;
using System.Collections;

public class WepShotgun : MonoBehaviour {

	public GameObject enemy;
	public Rigidbody projectile;
	public float speed = 40f;
	public float shootDelay = 0.5f;
	public int magazineSize = 3;
	public int currRounds = 3;
	public int totalAmmo = 90;
	public float timeAlive = 2f;
	public float gunSpread = 20f;
	public float tilt = 1f;
	public float reloadTime = 1f;
	private float counter = 0.0f;
	private bool reloading = false;
	private int currentWeapon = 1;
	public CrosshairControl ccobject;

	// Update is called once per frame
	public void FixedUpdate ()
	{

		if (!reloading && Input.GetButton ("Fire1") && counter > shootDelay && currRounds > 0) {
			ShottyBullet ();
			//ccobject.PlayAnim ();
			currRounds -= 1;
			counter = 0;
		} else if (Input.GetButtonDown ("Reload"))
		{	
			reloading = true;
			Invoke("Reload", reloadTime);
		}
		Debug.Log (currRounds);
		counter += Time.deltaTime;
	}

	void Reload ()
	{
		int difference = magazineSize - currRounds;
		if (totalAmmo - difference >= 0) {
			currRounds += difference;
			totalAmmo -= difference;
		} else if (totalAmmo - difference < 0) {
			currRounds = totalAmmo;
			totalAmmo = 0;
		}
		Debug.Log ("Total: " + totalAmmo);
		reloading = false;
	}


	void ShottyBullet ()
	{
		Debug.Log (transform.position + "   " + transform.rotation);

		Vector3 toZero = transform.TransformPoint (0, -0.3f, 1f);
		Vector3 toRight = transform.TransformPoint (0.1f, -0.3f, 1f);
		Vector3 toLeft = transform.TransformPoint (-0.1f, -0.3f, 1f);

		float zRightBullet = speed * Mathf.Cos(gunSpread * (Mathf.PI/180));
		float xRightBullet = speed * Mathf.Sin(gunSpread * (Mathf.PI/180));


		//var diagonalSpeed = Mathf.Pow(((speed * speed)/ 2), (0.5f));

		Rigidbody instantiatedProjectile = Instantiate (projectile, toZero, transform.rotation)as Rigidbody;
		instantiatedProjectile.velocity = transform.TransformDirection (new Vector3 (0, tilt, speed));

		Rigidbody instantiatedProjectileRight = Instantiate (projectile, toRight, transform.rotation)as Rigidbody;
		instantiatedProjectileRight.velocity = transform.TransformDirection (new Vector3 (xRightBullet, tilt, zRightBullet));

		Rigidbody instantiatedProjectileLeft = Instantiate (projectile, toLeft, transform.rotation)as Rigidbody;
		instantiatedProjectileLeft.velocity = transform.TransformDirection (new Vector3 (-xRightBullet, tilt, zRightBullet));

		Destroy (instantiatedProjectile.gameObject, timeAlive);
		Destroy (instantiatedProjectileRight.gameObject, timeAlive);
		Destroy (instantiatedProjectileLeft.gameObject, timeAlive);


	}
}
