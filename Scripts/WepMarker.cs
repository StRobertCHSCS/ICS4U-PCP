using UnityEngine;
using System.Collections;

public class WepMarker : MonoBehaviour {

	public GameObject enemy;
	public Rigidbody projectile;
	public float speed = 40f;
	public float shootDelay = 0.5f;
	public int currRounds = 90;
	public int totalAmmo = 90;
	public float timeAlive = 2f;
	public float gunSpread = 20f;
	public float tilt = 1f;
	public float reloadTime = 1f;
	public CrosshairControl ccobject;
	private float counter = 0.0f;
	private bool reloading = false;
	private int currentWeapon = 1;


	// Update is called once per frame
	public void FixedUpdate ()
	{

		if (!reloading && Input.GetButton ("Fire1") && counter > shootDelay && currRounds > 0) {
			
			Bullet ();
			//ccobject.PlayAnim ();
			currRounds -= 1;
			counter = 0;
		}
		Debug.Log (currRounds);
		counter += Time.deltaTime;
	}



	void Bullet ()
	{

		Vector3 toZero = transform.TransformPoint (0, 0, 1f);

		//var diagonalSpeed = Mathf.Pow(((speed * speed)/ 2), (0.5f));

		Rigidbody instantiatedProjectile = Instantiate (projectile, toZero, transform.rotation)as Rigidbody;
		instantiatedProjectile.velocity = transform.TransformDirection (new Vector3 (0, tilt, speed));

		Destroy (instantiatedProjectile.gameObject, timeAlive);
	}
}
