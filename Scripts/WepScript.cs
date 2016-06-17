using UnityEngine;
using System.Collections;

public class WepScript : MonoBehaviour
{
	public GameObject enemy;
	public Rigidbody projectile;
	public WepShotgun shotgun;
	public WepMarker marker;
	public WepMelee melee;
	public int currentWeapon = 2;


	// Update is called once per frame
	void Update ()
	{
		if (Input.GetKeyDown (KeyCode.Alpha1)) {
			currentWeapon = 1;
		} else if (Input.GetKeyDown (KeyCode.Alpha2)) {
			currentWeapon = 2;
		} else if (Input.GetKeyDown (KeyCode.Alpha3)) {
			currentWeapon = 3;
		}

		if (currentWeapon == 1) {
			melee.Update ();
		} else if (currentWeapon == 2) {
			shotgun.FixedUpdate ();
		} else if (currentWeapon == 3) {
			marker.FixedUpdate ();
		}
	}

}